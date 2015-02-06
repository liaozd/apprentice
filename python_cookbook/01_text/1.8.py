#!/usr/bin/python

# 1.8 Checking Whether a String Contains a Set of Characters

seq = "abcdefgh"
aset = 
def containsAny(seq, aset):
    """
    Check whether sequence seq contains ANY of the items in aset.
    """
    for c in seq:
        if c in aset: return True
    return False
  
