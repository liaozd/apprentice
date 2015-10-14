import struct

print struct.pack('hhl', 1, 2, 3)
# '\x01\x00\x02\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00'
print struct.unpack('hhl', '\x01\x00\x02\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00')
# (1, 2, 3)
print struct.calcsize('hhl')
# 8

theline = 'python cookbook'
baseformat = "5s 3x 8s 8s"
numremain = len(theline) - struct.calcsize(baseformat)
print struct.calcsize(baseformat)
format = "%s %ds" % (baseformat, numremain)
l, s1, s2, t = struct.unpack(format, theline)
