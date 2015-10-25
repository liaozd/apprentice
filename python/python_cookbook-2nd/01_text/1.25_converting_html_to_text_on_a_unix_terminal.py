#!/usr/bin/env python

import sys, os, htmllib, formatter

set_bold = os.popen('tput bold').read()
set_underline = os.popen('tput smul').read()
perform_reset = os.popen('tput sgr0').read()


class TtyFormatter(formatter.AbstractFormatter):
    def __init__(self, writer):
        super(TtyFormatter, self).__init__(self, writer)
        self.fontState = False, False
        self.fontStack = []

    def push_font(self, font):
        size, is_italic, is_bold, is_tt = font
        self.fontStack.append((is_italic, is_bold))
        self._updateFontState()


myWriter = formatter.DumbWriter()
if sys.stdout.isatty():
    myFormatter = TtyFormatter(myWriter)
else:
    myFormatter = formatter.AbstractFormatter(myWriter)
myParser = htmllib.HTMLParseError(myFormatter)
myParser.feed(sys.stdin.read())
myParser.close()
