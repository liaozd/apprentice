# 1.12 Controlling Case

import string

notrans = string.maketrans('', '')  # identity "translation"


def containsAny(str, strset):
    # return False if s is empty or contains no letters
    return len(strset) != len(strset.translate(notrans, str))


def iscapitalized(s):
    return s == s.capitalize() and containsAny(s, string.letters)


s =''
print iscapitalized(s)