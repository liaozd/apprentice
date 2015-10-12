#!/usr/bin/env python

# 1.6 Combining Strings
pieces = ['small1', 'small2', 'small3']
largeString = ''.join(pieces)
print largeString
'''
When you have many small string pieces in a sequence, performance can become a
truly important issue. The time needed to execute a loop using + or += (or a fancier
but equivalent approach using the built-in function reduce ) grows with the square of
the number of characters you are accumulating, since the time to allocate and fill a
large string is roughly proportional to the length of that string. Fortunately, Python
offers an excellent alternative.
'''

largeString = ''
for piece in pieces:
    largeString += piece
print largeString

# or, equivalently, but more fancifully and compactly:
import operator
largeString = reduce(operator.add, pieces, '')
print largeString


# 1.7 Reversing a String by Words or Characters
astring = 'abc  def ghi'
revchars = astring[::-1]
print revchars

revwords = astring.split()
print revwords
revwords.reverse()          # revers the list in place
print revwords
revwords = ' '.join(revwords)
print revwords

# or compact "one-liners"
revwords = ' '.join(astring.split()[::-1])
print "one-liners:", revwords

# preserving untouched the intermediate whitespaces
import re
revwords = re.split(r'(\s+)', astring)
print revwords
revwords.reverse()
print revwords
revwords = ''.join(revwords)
print revwords

# Bad one-liner code
revwords = ''.join(re.split(r'(\s+)', astring)[::-1])
print revwords
