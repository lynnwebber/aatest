#!/usr/bin/python
#
import operator

def caster(x):
    # print type(x)
    try:
        z = int(x)
        print "casted to:",z
        return z
    except:
        return x


def main():

    print "finding a numeric value in a list of strings and casting it to numeric or float"

    #    type_id,attribute,description,prod_mult,prod_type,slope,intercept
    #     int      str       str        int        int     float  float
    tmp = ['61','DP_IN_HG','Diffential Pressure','0','0','1','0']

    print [caster(x) for x in tmp]

# ------------------------------------------------------
if __name__ == "__main__":
    main()
