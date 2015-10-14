# 1.14 Changing the Indentation of a Multiline String


def reindent(s, numSpaces):
    leading_space = numSpaces * ' '
    lines = [leading_space + line.strip() for line in s.splitlines()]
    return '\n'.join(lines)


x = """ line one
   line two
      line 3
"""

print x
print reindent(x, 4)


def addSpaces(s, numAdd):
    white = " " * numAdd
    return white + white.join(s.splitlines(True))


def numSpaces(s):
    return [len(line) - len(line.lstrip()) for line in s.splitlines()]


def delSpaces(s, numDel):
    if numDel > min(numSpaces(s)):
        raise ValueError, "removing more spaces than there are!"
    return '\n'.join([line[numDel:] for line in s.splitlines()])


def unIndentBlock(s):
    return delSpaces(s, min(numSpaces(s)))


print unIndentBlock(x)
