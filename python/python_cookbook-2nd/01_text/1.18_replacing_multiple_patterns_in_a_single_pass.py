#!/usr/bin/env python

import re


def multiple_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))

    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)


# an closure-based version
def make_xlat(*args, **kwds):
    adict = dict(*args, **kwds)
    rx = re.compile('|'.join(map(re.escape, adict)))

    def one_xlat(match):
        return adict[match.group(0)]

    def xlat(text):
        return rx.sub(one_xlat, text)
    return xlat


# a class
class MakeXlat(object):
    def __init__(self, *args, **kwds):
        self.dict = dict(*args, **kwds)
        self.rx = self.make_rx()

    def make_rx(self):
        return re.compile('|'.join(map(re.escape, self.dict)))

    def one_xlat(self, match):
        return self.dict[match.group(0)]

    def __call__(self, text):
        return self.rx.sub(self.one_xlat, text)


if __name__ == "__main__":
    text = "Larry Wall is the creator of Perl"
    adict = {
        "Larry Wall": "Guido van Rossum",
        "creator": "Benevolent Dictator for Life",
        "Perl": "Python",
    }
    print multiple_replace(text, adict)

    # the closure-based
    translate = make_xlat(adict)
    print translate(text)

    # subclassing MakeXlat
    class MakeXlatByWholeWords(MakeXlat):
        def make_rx(self):
            return re.compile(r'\b{}\b'.format(r'\b|\b').join(map(re.escape, self.dict)))
    translate = MakeXlatByWholeWords(adict)
    print translate(text)
