__author__ = 'liao'

# 1.6 Combining Strings

pieces = ['small1', 'small2', 'small3']
largeString = ''.join(pieces)
print largeString


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

# preserving untouched the intermediate whitespace
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
