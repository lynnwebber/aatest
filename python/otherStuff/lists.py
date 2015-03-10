#!/usr/bin/python
#
import operator

print "for modifying a list of lists"

tqn = range(1,6)
a = [["PSD006",5], ["PSD007",3], ["PSD008",4], ["PSD009",6], ["PSD010",7]]
print tqn
print a
print map(lambda x,y: ['psd%03d' % y,x[1]], a, tqn)



print "\nstuff for finding range information"

a = range(0,304,30)
atb = [[x+1,x+30,0] for x in a]

tmp = [2,77,34,56,88,302,205,117,260,34]

for x in tmp:
    for b,t,cnt in atb:
        if (x > b) and (x < t):
            # get the index in the list
            ix = atb.index([b,t,cnt])
            # update the count
            cnt += 1
            atb[ix] = [b,t,cnt]
            break
        

for b,t,cnt in atb:
    print '%d   - between %d and %d' % (cnt,b,t)

print "\nstuff for sorting and disecting"
al = [["PSD006",5], ["PSD007",3], ["PSD008",4], ["PSD009",6], ["PSD010",7]]
bl = sorted(al,key=operator.itemgetter(1))
print 'best:',bl[:2]

bl = sorted(al,key=operator.itemgetter(1),reverse=True)
print 'worst first:',bl[:2]
