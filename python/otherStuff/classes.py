#!/usr/bin/python
#
import pdb


class teststore:
    def __init__(self):
        self.count = 0
        self.type = 'unknown'
        self.hdr = []
        self.scores = []

class storemgr:
    def __init__(self):
        self.typs = {}

    def storeScore(self,typ,quest,scor):
        if self.typs.has_key(typ):
            self.typs[typ].count += 1
            self.typs[typ].hdr.append(quest)
            self.typs[typ].scores.append(scor)
        else:
            self.typs[typ] = teststore()
            self.typs[typ].count += 1
            self.typs[typ].type = typ
            self.typs[typ].hdr.append(quest)
            self.typs[typ].scores.append(scor)
    

# ---- main -----
def main():
    print '-'*45+' start'
    tc = storemgr()
    tc.storeScore('IES','IES001','2')
    tc.storeScore('IES','IES002','4')
    tc.storeScore('IES','IES003','6')
    tc.storeScore('IES','IES004','8')
    tc.storeScore('IES','IES005','2')
    tc.storeScore('IES','IES006','3')
    
    tc.storeScore('IPT','IPT001','4')
    tc.storeScore('IPT','IPT002','4')
    tc.storeScore('IPT','IPT003','4')
    tc.storeScore('IPT','IPT004','4')

    for ky in tc.typs.keys():
        print tc.typs[ky].hdr
        print tc.typs[ky].scores

    print '-'*45+' end'


# ---------- run main -------------
if __name__ == "__main__":
    main()



