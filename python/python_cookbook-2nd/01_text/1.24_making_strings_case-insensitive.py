#!/usr/bin/env python


class iStr(str):

    def __init__(self, *args):
        self._lowered = str.lower(self)

    def __repr__(self):
        return '%s(%s)' % (type(self).__name__, str.__repr__(self))

    def __hash__(self):
        return hash(self._lowered)

    def lower(self):
        return self._lowered


def _make_case_insensitive(name):
    """
    wrap one method of str into an iStr one, case-insensitive
    """
    str_meth = getattr(str, name)

    def x(self, other, *args):
        try:
            other = other.lower()
        except (TypeError, AttributeError, ValueError):
            pass
        return str_meth(self._lowered, other, *args)

    setattr(iStr, name, x)

for name in 'eq lt le gt gt ne contains'.split():
    _make_case_insensitive('__%s__' % name)


s = iStr("abD")
# print s._lowered, id(s._lowered)
# print s, id(str)
print repr(s)
print type(s).__name__
