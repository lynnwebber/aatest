#!/usr/bin/python
#
import os, sys


cdl_block = """ChartType       = DIALCHART;
ChartName       = OverallPerformance;
Background	= (white,NONE,1,"null",TILE,black);
#Legend	        = (,black,"SansSerif",10,0);
#LegendItems	= ;
#LegendLayout    = (HORIZONTAL, BOTTOM);
LeftScale       = (25,75,100);
LeftTics        = (OFF,null,"SanSerif",10,0,null);
DwellLabel	= ("xx",white,"SansSerif",10,0);
DwellLabelBox	= (grey,RAISED,3,"null",TILE,black);
ColorTable	= x284b53,x005699,xb8bc9c,x271651,xaa0036,xecf0b9,x999966,x333366,xc3c3e6,x594330,xa0bdc4,x005699,x999966,x213321,x998300;
BackgroundFillPattern	= (NONE,null,null);
#ChartSize	= (450,400);
ChartSize = (400,400);
AntiAlias	= "ON";

#Header 	= ("Overall Recommendation",black,"SansSerif",12,0);
Header = ("Overall Recommendation",black,"SansSerif",12,0);

Dials 		= ("overall",-135,135,100,INSIDE),
		  ("base",-180,180,10,INSIDE);
DialBorders 	= ("overall",SOLID,2,lightgray,CNETER);
DialFills 	= ("overall",white,CENTER),
		  ("base",black,CENTER);
DialScale	= ("overall",0,100,5);
DialTicLabelStyles = ("overall",ON,1.1,BLACK,"Helvetica",10,0);
DialTicLabels	= ("overall","0",NULL,"10",NULL,"20",NULL,"30",NULL,"40",NULL,"50",NULL,"60",NULL,"70",NULL,"80",NULL,"90",NULL,"100");


Sectors		= ("Lowest",red,"overall",100,40),
		  ("Low",darkorange,"overall",100,40),
		  ("Moderate",royalblue,"overall",100,40),
		  ("High",green,"overall",100,40);
SectorData	= ("Lowest",0,25),
		  ("Low",25,50),
		  ("Moderate",50,75),
		  ("High",75,100);
SectorLabels	= ("Lowest","ON",0.7,white,"Helvetica",10,0),
		  ("Low","ON",0.7,white,"Helvetica",10,0),
		  ("Moderate","ON",0.7,white,"Helvetica",10,0),
		  ("High","ON",0.7,white,"Helvetica",10,0);

#Hands		= ("overall_hand",black,black,"overall");
#HandStyles	= ("overall_hand",BLOCK,8,4);
#HandData	= ("overall_hand",52,95);
Hands = ("overall_hand",black,black,"overall");
HandStyles = ("overall_hand",BLOCK,8,4);
"""


def main():
    thenum = '87.34'
    fl = open('blockwrite.txt','w')
    fl.write(cdl_block)
    hand = 'HandData= ("overall_hand",'+thenum+',95);'
    fl.write(hand)
    fl.close()

# ---------- run main -------------
if __name__ == "__main__":
    main()
