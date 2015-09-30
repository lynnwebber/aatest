#!/usr/bin/python
#
import os, sy

def check4value(xarray, num):
    try:
        pos = xarray.index(str(num))
        print "found it --> do nothing"
        print xarray
    except ValueError:
        print "not in the list adding it"
        xarray.append(str(num))
        print xarray




def main():

    print "strip the string and split into array"

    instring1 = "[23,34,45,56]"
    x = instring1.strip('[]')
    print x
    xarray = x.split(',')
    print xarray

    print "\narray search and test append"
    num = 23
    check4value(xarray,num)
    newnum = 33
    check4value(xarray,newnum)

    print "\n join back to string"
    z = "[" + ','.join(xarray) + "]"
    print z




# ------------------------------------------------------
if __name__ == "__main__":
    main()
