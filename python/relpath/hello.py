#!/usr/bin/python
#

def howdy():
    print "Howdy pilgrim."



def howyoudoin():
    print "how you doin?"


class Greetings:

    def __init__(self):
        self.g1 = 'the first greeting'
        self.g2 = 'the second greeting'

    def display(self,gn):
        if gn == 1:
            print self.g1
        elif gn == 2:
            print self.g2

greetings = Greetings()
