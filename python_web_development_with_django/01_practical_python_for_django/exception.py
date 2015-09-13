#!/usr/bin/env python

try:
    f = open(r'/tmp/filename.txt', 'r')
except IOError, e:
    print False, str(e)
finally:
    print 'Ending'

print f.readlines()

