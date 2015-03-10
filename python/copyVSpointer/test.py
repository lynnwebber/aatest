#!/usr/bin/env python
#


def test_func(td):
    rv = td.copy()
    rv['dd'] = 30
    print "original:", td
    print "second:", rv

    return rv







if __name__ == "__main__":

    a = '20031002045533'
    b = {'yy':a[:4],'MM':a[4:6],'dd':a[6:8]}

    c = test_func(b)



