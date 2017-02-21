#!/usr/bin/env python


def no_new_attributes(wrapped_setattr):
    """ raise an error on attempts to add a new attribute, while
        allowing existing attributes to be set to new values.
    """

    def __setattr__(self, name, value):
        if hasattr(self, name):  # not a new attribute, allow setting
            wrapped_setattr(self, name, value)
        else:
            raise AttributeError("can't add attribute %r to %s" % (name, self))
    return __setattr__


class NoNewAttrs(object):
    """ subclasses of NoNewAttrs inhibit addition of new attributes, while
        allowing existing attributed to be set to new values.
    """
    # lock the addition new atributes to instances of this class
    __setattr__ = no_new_attributes(object.__setattr__)

    class __metaclass__(type):
        """ simple custom metaclass to block adding new ttributes to this class
        """
        __setattr__ = no_new_attributes(type.__setattr__)


class Person(NoNewAttrs):
    firstname = ''
    lastname = ''

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        return 'Person(%r, %r)' % (self.firstname, self.lastname)

me = Person("Michere", "Simionato")
print me
me.firstname = "Michele"
print me

try:
    Person.address = 'Can not be set to class attr'
except AttributeError, err:
    print 'raised %r as expected' % err

try:
    me.address = 'Can not be set to instance attr'
except AttributeError, err:
    print 'rasied %r as expected' % err


