# 1.10 Filtering a String for a Set of Characters #"
import string


allchars = string.maketrans('', '')


def makefilter(keep):
    """ Return a function that takes a string and returns a partial copy
        of that string consisting of only the characters in 'keep'.
        Note that `keep' must be a plain string.
    """
    delchars = allchars.translate(allchars, keep)

    def thefilter(s):
        return s.translate(allchars, delchars)

    return thefilter


class Keeper(object):
    def __init__(self, keep):
        self.keep = set(map(ord, keep))

    def __getitem__(self, n):
        if n not in self.keep:
            return None
        return unichr(n)

    def __call__(self, s):
        return unicode(s).translate(self)

if __name__ == '__main__':
    just_vowels = makefilter('aeiouy')
    print just_vowels('four score and seven years ago')
    print len(allchars.translate(allchars))
    print makefilter('four score and seven years ago')(allchars)

    just_vowels = Keeper('aeiouy')
    print just_vowels(u'four score and seven years ago')
