#!/usr/bin/env python

# ref: http://blaag.haard.se/What-s-the-point-of-properties-in-Python/
# ref: http://www.python-course.eu/python3_properties.php


class PositiveNum(object):

    def __init__(self, x):
        self.set_value(x)

    def get_value(self):
        return self.__y

    def set_value(self, x):
        if x < 0:
            self.__y = 0
        else:
            self.__y = x


pn = PositiveNum(100)
print pn.get_value()


class PositivePropertyNum(object):

    def __init__(self, x):
        self.value = x

    @property
    def value(self):
        return self.__y

    @value.setter
    def value(self, x):
        if x < 0:
            self.__y = 0
        else:
            self.__y = x


ppn = PositivePropertyNum(100)
print ppn.value
ppn.value = -100
print ppn.value


