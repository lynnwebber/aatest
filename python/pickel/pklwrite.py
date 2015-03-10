#!/usr/bin/python
#
import cPickle

multiDict = {}
    
def addMultiStmt(dim,match):
    multiDict[dim.lower()] = match

def getMultiStmt(dim):
    return multiDict[dim.lower()]



# ---- main -----
def main():
    '''
    create a class of statements
    pickle the class for use with another program to read the class
    '''
    addMultiStmt('Achevement',{'match':'this is a statement for achevement'})
    addMultiStmt('Intuition',{'match':'this is a statement for intuition'})
    addMultiStmt('Ambition',{'match':'this is a statement for ambition'})
    addMultiStmt('Play',{'match':'this is a statement for Play'})

    pklfl = open('statements.pkl','wb')
    cPickle.dump(multiDict,pklfl)
    pklfl.close()

# ---------- run main -------------
if __name__ == "__main__":
    main()
