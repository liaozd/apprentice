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