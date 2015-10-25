#!/usr/bin/env python

import itertools
import os


def anyTrue(predicate, sequence):
    return True in itertools.imap(predicate, sequence)


def endsWith(s, *endings):
    return anyTrue(s.endswith, endings)

for filename in os.listdir('/tmp'):
    if endsWith(filename, '.jpg', '.jpeg', '.gif', '.png'):
        print filename
