#!/usr/bin/env python
import re

thefilepath = '/var/log/wtmp'

# 1
re_word = re.compile(r"[\w'-]+")
print re_word
for line in open(thefilepath):
    for word in re_word.finditer(line):
        print word.group(0)


def words_of_file(thefilepath, line_to_words=str.split):
    the_file = open(thefilepath)
    for line in the_file:
        for word in line_to_words(line):
            yield word
    the_file.close()
for word in words_of_file(thefilepath):
    print word


def words_by_re(thefilepath, repattern=r"[\w'-]+"):
    wre = re.compile(repattern)

    def line_to_words(line):
        for mo in wre.finditer(line):
            yield mo.group(0)
    return words_of_file(thefilepath, line_to_words)

