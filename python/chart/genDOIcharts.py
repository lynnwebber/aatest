#!/usr/bin/python
#
#
"""
genDOIcharts.py

  Designed to read the chart information from a doi report data xml file
  and generate the charts/graphs for that document 

Usage
  genDOIcharts.py [options]

Options
  -h, --help - print usage information
  -d, --dir - output directory, defaults to current directory
  -i, --input - doi report data xml file (required)
  -v, --verbose - print robust run information
"""
#
import sys
import os
import string
import getopt
import xml.etree.ElementTree as et
from pychart import *

# ----------------------------------------------------------------
# usage
#
def usage(): print __doc__


# ----------------------------------------------------------------
# check/get/set command line options
#
def getCommandLine():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:d:hv",
                                   ["input=","dir=","help","verbose"])
    except getopt.GetoptError:
        print "\nInvalid argument"
        usage()
        sys.exit(2)

    requiredCount = 0

    verbose = False
    outdir = ""
    infile = "??"

    if len(opts) == 0:
        print "\nNo arguments passed"
        usage()
        sys.exit(2)
    
    for o, a in opts:
        if o in ("-v", "--verbose"):
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit(2)
        elif o in ("-i", "--input"):
            infile = a
            requiredCount += 1
        elif o in ("-d", "--dir"):
            outdir = a
        else:
            assert False, "unknown option passed"

    if requiredCount < 1:
        print "\nOne or more required arguments missing"
        usage()
        sys.exit(2)

    return verbose, infile, outdir


# ----------------------------------------------------------------
# General use functions and/or classes 
#
def read_infile(fn):
    xmlstr = ''
    fobj = open(fn,'r')

    for line in fobj:
        xmlstr += line.strip()
    fobj.close()
    return xmlstr

# ----------------------------------------------------------------
def make_fn(dir,seed,type):
    rv = ''
    ftype = '.png'
    if type == 'factor':
        rv = "%s/%s_factor%s" % (dir,seed,ftype)
    elif type == 'subscale':
        rv = "%s/%s_subscale%s" % (dir,seed,ftype)
    elif type == 'overall':
        rv = "%s/DOI_overall%s" % (dir,ftype)
    else:
        rv = "invalid_type_file_name"

    return rv

# ----------------------------------------------------------------
class doi_rpt_xml_mgr:

    def __init__(self):
        self.tree = ''
        self.ov_graph = ''
        self.indv_graphs = ''

    def parse(self,xmlstr):
        try:
            self.tree = et.fromstring(xmlstr)
        except:
            return False
        self.ov_graph = self.get_overall_graph_data()
        self.ov_graph.reverse()
        self.indv_graphs = self.get_fac_and_subs()
        return True


    def get_overall_graph_data(self):
        rv = []
        xpth = 'report/overall_graph/items'
        itms = self.tree.find(xpth)
        for x in list(itms):
            nam = x.tag.title()
            scor = float(x.get('value'))
            rv.append([nam,scor])
        return rv

    def get_fac_and_subs(self):
        rv = []
        xpth = 'report/factors'
        facs = self.tree.find(xpth)
        for x in list(facs):
            nam = x.tag.title()
            scor = float(x.findtext("score"))
            labl = x.findtext("graph_labels")

            subs = x.find("subscales")
            subrv = []
            for i in list(subs):
                sub = i.tag.title()
                subscor = float(i.findtext("score"))
                sublbls = i.findtext("graph_label")
                subrv.append([sub,subscor,sublbls])

            rv.append([[nam,scor,labl],subrv])
        return rv

# ----------------------------------------------------------------
# GRAPHICS ROUTINES
# -------------------------------------------------------------
# globals used for fill styles so all the graphs are the same
#   the following table corresponds to an 8 bit color palet
#   0 --> 0x0 --> 0
#   3 --> 0x3 --> 0.1
#   6 --> 0x6 --> 0.3
#   9 --> 0x9 --> 0.5
#   12 --> 0xc --> 0.7
#   15 --> 0xf --> 1

myfs = fill_style.Plain(bgcolor=color.white)
shadow_fill = fill_style.Plain(bgcolor=color.slategray)
line_fill = fill_style.Plain(bgcolor=color.T(r=0,g=0,b=0.7)) #063
verystrong_fill = fill_style.Plain(bgcolor=color.T(r=1,g=0.5,b=0.5)) #f99
strong_fill = fill_style.Plain(bgcolor=color.T(r=1,g=0.7,b=0.5)) #fc9
moderate_fill = fill_style.Plain(bgcolor=color.T(r=1,g=1,b=0.7)) #ffc
average_fill = fill_style.Plain(bgcolor=color.T(r=0.7,g=1,b=0.7))    #cfc


# ----------------------------------------------------------------
# summary_graph 
#
def draw_overall_graph(data,fn):

    theme.use_color = True
    theme.output_format="png"
    theme.output_file=fn
    theme.reinitialize()

    # create the canvis for the drawing 
    can = canvas.default_canvas()

    # set the chart area size
    chart_object.set_defaults(area.T,size=(420,200))

    # The attribute y_coord_system="category" tells that the Y axis values
    # should be taken from samples, y_category_col'th column of
    # y_category_data.  
    ar = area.T(y_coord = category_coord.T(data, 0),
                x_grid_style=None,          #line_style.gray90_dash2,
                x_grid_interval=5,
                x_range = (20,80), 
                x_axis=axis.X(label="Standard Factor Scores"),
                y_grid_style=None,
                y_axis=axis.Y(label=""),
                #bg_style = myfs,
                border_line_style = line_style.default,
                legend = None) 

    # Below call sets the default attributes for all bar plots.
    chart_object.set_defaults(bar_plot.T, direction="horizontal", data=data)

    # plot the data on the chart
    blst = []
    for x,y in data:
        pl = bar_plot.T(data=[(x,y)],width=11,fill_style=line_fill)
        blst.append(pl)
        continue

    for x in blst:
        ar.add_plot(x)

    # setup the parameters for drawing the color range boxes
    xloc = ar.loc[0]
    ytip = ar.loc[1] + ar.size[1]  # + 15
    ybot = ar.loc[1] # - 20

    # draw the color range boxes
    can.rectangle(line_style.default,verystrong_fill,xloc,ybot,ar.x_pos(30),ytip)
    can.rectangle(line_style.default,strong_fill,ar.x_pos(30),ybot,ar.x_pos(40),ytip)
    can.rectangle(line_style.default,moderate_fill,ar.x_pos(40),ybot,ar.x_pos(47),ytip)
    can.rectangle(line_style.default,average_fill,ar.x_pos(47),ybot,ar.x_pos(53),ytip)
    can.rectangle(line_style.default,moderate_fill,ar.x_pos(53),ybot,ar.x_pos(60),ytip)
    can.rectangle(line_style.default,strong_fill,ar.x_pos(60),ybot,ar.x_pos(70),ytip)
    can.rectangle(line_style.default,verystrong_fill,ar.x_pos(70),ybot,ar.x_pos(80),ytip)
    
    # draw the chart area (over the top of the color range boxes)
    ar.draw()

    # setup the parameters for drawing the text boxes that point to the ranges
    yloc = ar.loc[1] + ar.size[1] + 35
    ytip = ar.loc[1] + ar.size[1]

    def describeThreashold(thold,label,off,shadow_fs):
        x1 = ar.x_pos(thold)
        tb = text_box.T(text=label, loc=(x1+off, yloc), shadow=(2,-2,shadow_fs))
        tb.add_arrow((x1, ytip))
        tb.draw()
        
    describeThreashold(25, "Very Strong\nLow", -80, shadow_fill)
    describeThreashold(35, "Strong\nLow", -50, shadow_fill)
    describeThreashold(44, "Moderate\nLow", -45, shadow_fill)
    describeThreashold(50, "Average", -25, shadow_fill)
    describeThreashold(56, "Moderate\nHigh", 0, shadow_fill)
    describeThreashold(65, "Strong High", 35, shadow_fill)
    describeThreashold(75, "Very Strong\nHigh", 50, shadow_fill)

    can.close()

# ----------------------------------------------------------------
# factor graph
#
def draw_factor_graph(indata,glabels,fn):

    data = []
    for x,y in indata:
        gtitle = x
        data.append(['',y])

    theme.use_color = True
    theme.output_format="png"
    theme.output_file=fn
    theme.reinitialize()

    # create the canvis for the drawing 
    can = canvas.default_canvas()

    # set the chart area size
    chart_object.set_defaults(area.T,size=(420,40))

    # The attribute y_coord_system="category" tells that the Y axis values
    # should be taken from samples, y_category_col'th column of
    # y_category_data.  
    ar = area.T(y_coord = category_coord.T(data, 0),
                x_grid_style=None,
                x_grid_interval=None,
                x_range = (20,80), 
                x_axis=axis.X(label=""),
                y_grid_style=None,
                y_axis=axis.Y(label=""),
                border_line_style = line_style.default,
                legend = None) 

    # Below call sets the default attributes for all bar plots.
    chart_object.set_defaults(bar_plot.T, direction="horizontal", data=data)

    # plot the data on the chart
    blst = []
    for x,y in data:
        pl = bar_plot.T(data=[(x,y)],width=11,fill_style=line_fill)
        blst.append(pl)

    for x in blst:
        ar.add_plot(x)

    # setup the parameters for drawing the color range boxes
    xloc = ar.loc[0]
    ytip = ar.loc[1] + ar.size[1] #+ 15
    ybot = ar.loc[1] #- 20

    # draw the color range boxes
    can.rectangle(line_style.default,verystrong_fill,xloc,ybot,ar.x_pos(30),ytip)
    can.rectangle(line_style.default,strong_fill,ar.x_pos(30),ybot,ar.x_pos(40),ytip)
    can.rectangle(line_style.default,moderate_fill,ar.x_pos(40),ybot,ar.x_pos(47),ytip)
    can.rectangle(line_style.default,average_fill,ar.x_pos(47),ybot,ar.x_pos(53),ytip)
    can.rectangle(line_style.default,moderate_fill,ar.x_pos(53),ybot,ar.x_pos(60),ytip)
    can.rectangle(line_style.default,strong_fill,ar.x_pos(60),ybot,ar.x_pos(70),ytip)
    can.rectangle(line_style.default,verystrong_fill,ar.x_pos(70),ybot,ar.x_pos(80),ytip)
    
    # draw the chart area (over the top of the color range boxes)
    ar.draw()
    
    # write the subscale title information at the top of the canvas
    txtout = "/10/b/hC%s Factor" % (gtitle.title())
    can.show(ar.x_pos(50),ytip+10,txtout)

    # write over the flipping grid intervals on graph so that we can
    #  put in the unique text for the factor
    can.rectangle(None,myfs,xloc-5,ybot-15,ar.x_pos(80)+5,ybot-1)

    xbase = [ar.x_pos(30),ar.x_pos(40),ar.x_pos(50),ar.x_pos(60),ar.x_pos(70)]
    ll = zip(glabels,xbase)
    for txt,base in ll:
        txtout = '/8/hC'+txt
        can.show(base,ybot-10,txtout)

    can.close()

# ----------------------------------------------------------------
# subscale graph
#
def draw_subscale_graph(indata,glabels,fn):

    data = []
    for x,y in indata:
        gtitle = x
        data.append(['',y])

    theme.use_color = True
    theme.output_format="png"
    theme.output_file=fn
    theme.reinitialize()

    # create the canvis for the drawing 
    can = canvas.default_canvas()

    # set the chart area size
    chart_object.set_defaults(area.T,size=(420,40))

    # The attribute y_coord_system="category" tells that the Y axis values
    # should be taken from samples, y_category_col'th column of
    # y_category_data.  
    ar = area.T(y_coord = category_coord.T(data, 0),
                x_grid_style=None,
                x_grid_interval=None,
                x_range = (20,80), 
                x_axis=axis.X(label=""),
                y_grid_style=None,
                y_axis=axis.Y(label=""),
                border_line_style = line_style.default,
                legend = None) 

    # Below call sets the default attributes for all bar plots.
    chart_object.set_defaults(bar_plot.T, direction="horizontal", data=data)

    # plot the data on the chart
    blst = []
    for x,y in data:
        pl = bar_plot.T(data=[(x,y)],width=11,fill_style=line_fill)
        blst.append(pl)

    for x in blst:
        ar.add_plot(x)

    # setup the parameters for drawing the color range boxes
    xloc = ar.loc[0]
    ytip = ar.loc[1] + ar.size[1] #+ 15
    ybot = ar.loc[1] #- 20

    # draw the color range boxes
    can.rectangle(line_style.default,verystrong_fill,xloc,ybot,ar.x_pos(30),ytip)
    can.rectangle(line_style.default,strong_fill,ar.x_pos(30),ybot,ar.x_pos(40),ytip)
    can.rectangle(line_style.default,moderate_fill,ar.x_pos(40),ybot,ar.x_pos(47),ytip)
    can.rectangle(line_style.default,average_fill,ar.x_pos(47),ybot,ar.x_pos(53),ytip)
    can.rectangle(line_style.default,moderate_fill,ar.x_pos(53),ybot,ar.x_pos(60),ytip)
    can.rectangle(line_style.default,strong_fill,ar.x_pos(60),ybot,ar.x_pos(70),ytip)
    can.rectangle(line_style.default,verystrong_fill,ar.x_pos(70),ybot,ar.x_pos(80),ytip)
    
    # draw the chart area (over the top of the color range boxes)
    ar.draw()
   
    # write the subscale title information at the top of the canvas
    txtout = "/10/b/hC%s" % (gtitle.title())
    can.show(ar.x_pos(50),ytip+10,txtout)

    # write over the flipping grid intervals on graph so that we can
    #  put in the unique text for the factor
    can.rectangle(None,myfs,xloc-5,ybot-15,ar.x_pos(80)+5,ybot-1)

    xbase = [ar.x_pos(30),ar.x_pos(40),ar.x_pos(50),ar.x_pos(60),ar.x_pos(70)]
    ll = zip(glabels,xbase)
    for txt,base in ll:
        ## do something here to deal with long strings usually
        ## in the average labels but could be in other places
        if len(txt) > 22:
            z = txt.split()
            if string.count(txt,' ') > 1:
                x = "%s\n%s" % (string.join(z[:2]),string.join(z[2:]))
                txtout = '/8/hC'+x
            else:
                x = "%s\n%s" % (string.join(z[:1]),string.join(z[1:]))
                txtout = '/8/hC'+x
            tbot = ybot-17
        else:
            txtout = '/8/hC'+txt
            tbot = ybot-10
        can.show(base,tbot,txtout)

    can.close()


# ----------------------------------------------------------------
# main program module
#
def main():

    # get all the stuff from the command line
    #
    verbose,infile,outdir = getCommandLine()
    doi = doi_rpt_xml_mgr()

    # get the input xml file and hand it to an instance of the 
    # data management class
    #
    xmldat = read_infile(infile)
    doi.parse(xmldat)

    # ------ generate the overall graph here ------

    outfile = make_fn(outdir,"na","overall")
    draw_overall_graph(doi.ov_graph,outfile)

    for x in doi.indv_graphs:
        fac = x[0][0]
        outfile = make_fn(outdir,fac,'factor')
        ftmp = x[:1]
        for i in ftmp:
            flst = i[:2]
            lbl = i[2:][0].split('|')
            draw_factor_graph([flst],lbl,outfile)

    for x in doi.indv_graphs:
        fac = x[0][0]
        stmp = x[1]
        for i in stmp:
            subs = i[0]
            outfile = make_fn(outdir,subs,'subscale')
            slst = i[:2]
            lbl = i[2].split('|')
            draw_subscale_graph([slst],lbl,outfile)


# ----------------------------------------------------------------
#  run main
#
if __name__ == "__main__": main()
