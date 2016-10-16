#!/usr/bin/env python

"""
When to use __new__ vs. __init__ ?

Use __new__ when you need to control the creation of a new instance.
Use __init__ when you need to control initialization of a new instance.

__new__ is the first step of instance creation.  It's called first,
and is responsible for returning a new instance of your class.  In
contrast, __init__ doesn't return anything; it's only responsible for
initializing the instance after it's been created.

In general, you shouldn't need to override __new__ unless you're
subclassing an immutable type like str, int, unicode or tuple.

Some references:
The description of new style classes goes into some depth about how
instance creation works, including examples of overriding __new__ and
__init__. http://www.python.org/download/releases/2.2/descrintro/

The reference manual has a section on class customization, but I don't
think it goes into enough depth to really answer your question:
http://docs.python.org/ref/customization.html

3.4.1. Basic customization:
https://docs.python.org/2/reference/datamodel.html#basic-customization

Understanding __new__ and __init__
http://spyhce.com/blog/understanding-new-and-init
"""


class BaseMeta(object):
    _dict = dict()

    def __new__(cls):
        if 'key' in BaseMeta._dict:
            print "EXISTS"
            return BaseMeta._dict['key']
        else:
            print "NEW"
            return super(BaseMeta, cls).__new__(cls)

    def __init__(self):
        print "INIT"
        BaseMeta._dict['key'] = self
        print ""

a1 = BaseMeta()
a2 = BaseMeta()
a3 = BaseMeta()

