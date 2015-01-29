#!/usr/bin/python
import inspect


def wrap_callable(any_callable, before, after):
    """wrap any callable with before/after calls"""
    def _wrapped(*a, **kw):
        before()
        try:
            return any_callable(*a, **kw)
        finally:
            after()
    return _wrapped


class GenericWrapper(object):
    """ wrap all of an object's methods with before/after calls
    """
    def __init__(self, obj, before, after, ignore=()):
        # we must set into __dict__ directly to bypass __setattr__; so,
        # we need to reproduce the name-mangling for double-underscores
        clasname = 'GenericWrapper'
        self.__dict__['_%s__methods' % clasname] = {}
        self.__dict__['_%s__obj' % clasname] = obj
        for name, method in inspect.getmembers(obj, inspect.ismethod):
            if name not in ignore and method not in ignore:
                self.__methods[name] = wrap_callable(method, before, after)

    def __getattr__(self, name):
        try:
            return self.__methods[name]
        except KeyError:
            return getattr(self.__obj, name)

    def __setattr__(self, name, value):
        setattr(self.__obj, name, value)


class SynchronizedObject(GenericWrapper):
    """ wrap an object and all of its methods with synchronization
    """
    def __init__(self, obj, ignore=(), lock=None):
        if lock is None:
            import threading
            lock = threading.RLock()
        GenericWrapper.__init__(self, obj, lock.acquire, lock.release, ignore)

if __name__ == '__main__':
    import threading
    import time
    class Dummy(object):
        def foo(self):
            print 'hello from foo'
            time.sleep(1)
        def bar(self):
            print 'hello from bar'
        def baaz(self):
            print 'hello from baaz'
    tw = SynchronizedObject(Dummy(), ignore=['baaz'])
    threading.Thread(target=tw.foo).start()
    time.sleep(0.1)
    threading.Thread(target=tw.bar).start()
    time.sleep(0.1)
    threading.Thread(target=tw.baaz).start()
