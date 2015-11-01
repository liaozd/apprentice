#!/usr/bin/env python

import struct

format_string = '8l'
thefile = open('somebinfile', 'r+b')
record_size = struct.calcsize(format_string)
record_number = 6
thefile.seek(record_size * record_number)
buffer = thefile.read(record_size)
fields = list(struct.unpack(format_string, buffer))
# Perform computations, suitably modifying fields, then:
buffer = struct.pack(format_string, *fields)
thefile.seek(record_size * record_number)
thefile.write(buffer)
thefile.close()
