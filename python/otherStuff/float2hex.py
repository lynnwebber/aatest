#!/usr/bin/python
#
import os, sys
import struct

def conv32bit_big(x):
    z = struct.pack('>f',x)
    z2 = ''.join('%.2x' % ord(c) for c in z)
    print "32-bit big endian: 0x%s"  % (z2)

def conv32bit_little(x):
    z = struct.pack('<f',x)
    z2 = ''.join('%.2x' % ord(c) for c in z)
    print "32-bit little endian: 0x%s"  % (z2)

def main():

    print "print fp to hex conversions"
    conv32bit_big( float(sys.argv[1]) )
    conv32bit_little( float(sys.argv[1]) )

# ------------------------------------------------------
if __name__ == "__main__":
    main()
