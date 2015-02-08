#!/usr/bin/python
from timeit import Timer

# 1.8 Checking Whether a String Contains a Set of Characters

seq = "abcdefgh"
aset = "bcd"


def containsAny1(seq, aset):
    """
    Check whether sequence seq contains ANY of the items in aset.
    """
    for c in seq:
        if c in aset: return True
    return False

t1 = Timer("containsAny1(seq, aset)", "from __main__ import containsAny1, seq, aset")
print "containsAny1 time: ", t1.timeit()


# cookbook says this a quick way, but it doesn't
import itertools


def containsAny2(seq, aset):
    for item in itertools.ifilter(aset.__contains__, seq):
        """
        itertools.ifilter(predicate, iterable)
        Make an iterator that filters elements from iterable returning only
        those for which the predicate is True. If predicate is None, return
        the items that are true.
        """
        return True
    return False
t2 = Timer("containsAny2(seq, aset)", "from __main__ import containsAny2, seq, aset")
print "containsAny2 time: ", t2.timeit()


# a pure set-based approach:
def containsAny3(seq, aset):
    return bool(set(aset).intersection(seq))
t3 = Timer("containsAny3(seq, aset)", "from __main__ import containsAny3, seq, aset")
print "containsAny3 time: ", t3.timeit()
print
print "set(aset).intersection(seq):", set(aset).intersection(seq)
# a.difference(b) equall to set(a) - set(b)
print "set(aset).difference(seq): ", set(aset).difference(seq)
print "set(seq).intersection(aset):", set(seq).intersection(aset)

def containsALL(seq, aset):
    """
    Check whether sequence seq contains All the items in aset.
    """
    return not set(aset).difference(seq)


# http://stackoverflow.com/questions/25626694/python-2-7-writing-x-in-set-vs-set-contains-x
import dis
print 'b.__contains__(i)'
dis.dis(compile('b.__contains__(i)', '<>', 'exec'))
print 'i in s'
dis.dis(compile('i in s', '<>', 'exec'))

print
print "string.maketrans method"
import string
notrans = string.maketrans('','')
# string.maketrans(from, to)
# Return a translation table suitable for passing to translate(),
# that will map each character in from into the character at the
# same position in to; from and to must have the same length.
def containsAnyStr(astr, strset):
    return len(strset) != len(strset.translate(notrans, astr))
    # str.translate(table[, deletechars])
    # Return a copy of the string where all characters occurring
    # in the optional argument deletechars are removed, and the
    # remaining characters have been mapped through the given
    # translation table, which must be a string of length 256.
def containsAll(astr, strset):
    return not strset.translate(notrans, astr)
t4 = Timer("containsAnyStr(seq, aset)", "from __main__ import containsAnyStr, seq, aset")
print "containsAnyStr time: ", t4.timeit()



# 1.9 Simplifying Usage of Strings’ translate Method
