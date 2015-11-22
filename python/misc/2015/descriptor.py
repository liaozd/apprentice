#!/usr/bin/env python


class Descriptor(object):
    def __get__(self, obj, type=None):
        print ('get:', self, obj, type)

    def __set__(self, obj, value):
        print('set:', self, obj, value)

    def __delete__(self, obj):
        print('delete:', self, obj)


class T(object):
    d = Descriptor()
t = T()

t.d = 'hello'
print t.__dict__
