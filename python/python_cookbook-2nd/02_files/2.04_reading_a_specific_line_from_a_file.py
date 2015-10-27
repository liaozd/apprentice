#!/usr/bin/env python

import linecache
filepath, linenum = "/tmp/tmp.txt", 2

theline = linecache.getline(filepath, linenum)
print theline


def getline(thefilepath, desired_line_number):
    if desired_line_number < 1:
        return ''
    for current_line_number, line in enumerate(open(thefilepath, 'rU')):
        if current_line_number == desired_line_number - 1:
            return line
    return ''

print getline(filepath, linenum)
