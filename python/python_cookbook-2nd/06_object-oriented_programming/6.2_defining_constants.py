#!/usr/bin/env python
# Save this code as module const.py on some directory on your Python sys.path


class _const(object):
    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError, "Can't rebind const(%s)" % name
        self.__dict__[name] = value

    def __delattr__(self, name):
        if name in self.__dict__:
            raise self.ConstError, "Can't delete const(%s)" % name
        raise NameError, name

import sys
sys.modules[__name__] = _const()
