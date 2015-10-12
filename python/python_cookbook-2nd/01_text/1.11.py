# 1.11 Checking Whether a String Is Text or Binary
from __future__ import division
import string

text_characters = "".join(map(chr, range(32,127))) + "\n\r\t\b"
_null_trans = string.maketrans("","")


def istext(s, text_characters=text_characters, threshold=0.30):
    # if s contains any null, it's not text
    if "\0" in s:
        return False
    # an "empty" string is "text" (arbitratry but reasonable choice):
    if not s:
        return True
    # Get the substring of s made up of non-text characters
    t = s.translate(_null_trans, text_characters)
    return len(t)/len(s) <= threshold


def istextfile(filename, blocksize=512, **kwds):
    return istext(open(filename).read(blocksize), **kwds)

print istextfile('/git-repos/apprentice/python/python_cookbook-2nd/01_text/1.08-1.09.py')
print istextfile("/git-repos/apprentice/python/djangoproject_com/db.sqlite3")