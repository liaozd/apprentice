#!/usr/bin/env python

# 1.1 Processing a String One Character at a Time
print "C1.1"
thestring = "abcdefghijklmn"

# list comprehension
resultA = [ c+"." for c in thestring ]

import sets
magic_chars = sets.Set('abracadabra')
poppins_chars = sets.Set('supercalifgrailisticexpialidocious')
set_intersection = magic_chars & poppins_chars
print ''.join(set_intersection)

# 1.2 Converting Between Characters and Numeric Codes
print "C1.2"
print ord('a')
print chr(97)
print ord(u'\u2020')
print repr(unichr(8224))
print "map(ord, 'ciao')", map(ord, 'ciao')
print ''.join(map(chr, range(97, 120)))

# 1.3 Testing Whether an Object Is String-like
print "C1.3"


def isAString(anobj):
    return isinstance(anobj, basestring)


def isExactlyAString(anobj):
    # bad approach, unicode test fail
    return type(anobj) is type('')

u_str = unicode('abcde')

print isAString(u_str), isExactlyAString(u_str)


def isStringLike(anobj):
    # the general Python approach to type-checking is known as
    # duck typing: if it walks like a duck and quacks like a duck,
    # it's duck-like enough for our purpose.
    try:
        anobj.lower() + anobj + ''
    except:
        return False
    else:
        return True

import UserString
usr_str = UserString.UserString("userstring")
print isAString(usr_str)
print isStringLike(usr_str)

# 1.4 Aligning Strings
print '|', "Left".ljust(20),'|', 'Right'.rjust(20), '|', 'Center'.center(20),'|'
print ' Center '.center(20,'+')

# 1.5 Trimming Space from the Ends of a String
x = '   hej   '
print '|', x.lstrip(), '|', x.rstrip(), '|', x.strip(), '|'

x = 'xyxxyy hejxy yyx'
print '|' + x.strip('xy') + '|'