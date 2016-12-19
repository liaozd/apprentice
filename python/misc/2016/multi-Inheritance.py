class APIBaseClassOne(object):
    def __init__(self, *args, **kwargs):
        print (" base ")


class SomeMixin(object):
    def __init__(self, *args, **kwargs):
        print (" mixin before ")
        super(SomeMixin, self).__init__(*args, **kwargs)
        print (" mixin after ")


class MyClass(APIBaseClassOne):
    pass


class MixedClass(SomeMixin, MyClass,):
    pass


class MyClassFirstClass(MyClass, SomeMixin,):
    pass

m = MixedClass()
print "=" * 20
MyClassFirstClass()
