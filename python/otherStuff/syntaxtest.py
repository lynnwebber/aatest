#!/usr/bin/python
#

import sys

def multi_line_if(x):
    if x in ("yes",
            "no",
            "maybe"):
        print "found it"
    else:
        print "not found"


# ---- main -----
def main():
    multi_line_if('dog')
    multi_line_if('maybe')

# ---------- run main -------------
if __name__ == "__main__":
    main()
