#!/usr/bin/python
#
import cPickle


# ---- main -----
def main():
    '''
    create a class of statements
    pickle the class for use with another program to read the class
    '''

    pklfl = open('statements.pkl','rb')
    md = cPickle.load(pklfl)
    pklfl.close()

    print 'pickled object full data:',md
    print 'data for intuition:',md['intuition']['match']
    

# ---------- run main -------------
if __name__ == "__main__":
    main()
