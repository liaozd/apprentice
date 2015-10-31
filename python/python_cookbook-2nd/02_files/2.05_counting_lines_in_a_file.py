#!/usr/bin/env python

import time, os


def timeo(fun, n=10):
    start = time.clock()
    for i in xrange(n):
        fun()
    stend = time.clock()
    thetime = stend - start
    return fun.__name__, thetime

testfile = '/var/log/dpkg.log'


def linecount_w():
    return int(os.popen('wc -l {}'.format(testfile)).read().split()[0])


def linecount_1():
    return len(open(testfile).readlines())


def linecount_2():
    count = -1
    for count, line in enumerate(open(testfile)):
        pass
    return count + 1


def linecount_3():
    count = 0
    thefile = open(testfile, 'rb')
    while True:
        buffer = thefile.read(65536)
        if not buffer:
            break
        count += buffer.count('\n')
    return count

for f in linecount_w, linecount_1, linecount_2, linecount_3:
    print f.__name__, f()
for f in linecount_1, linecount_2, linecount_3:
    print "%s: %.2f" % timeo(f)
