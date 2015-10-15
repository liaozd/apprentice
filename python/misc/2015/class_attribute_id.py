class Parent(object):
    x = 1


class Child1(Parent):
    pass


class Child2(Parent):
    pass

print "Parent.x id(Parent.x) Child1.x id(Child1.x) Child2.x id(Child2.x)"
print Parent.x, id(Parent.x), Child1.x, id(Child1.x), Child2.x, id(Child2.x)
Child1.x = 2
print Parent.x, id(Parent.x), Child1.x, id(Child1.x), Child2.x, id(Child2.x)
Parent.x = 3
print Parent.x, id(Parent.x), Child1.x, id(Child1.x), Child2.x, id(Child2.x)
