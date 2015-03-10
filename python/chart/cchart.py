#!/usr/bin/python
#
from pychart import *

class summary_page:

    def __init__(self):
        self.can = canvas.init("summary.png")

    def draw_can(self):
        self.can.close()

    def draw_test1(self):
        xsiz = 150
        ysiz = 120
        
        theme.get_options()
        theme.use_color = True
        theme.reinitialize()

        data = [("Conceiving","Applying",52.9226328809),("Interacting","Contemplating",60.6060413003),
                ("Engaging","Distancing",44.6717376408),("Collaborating","Driving",47.1748466538),
                ("Adapting","Structuring",64.0713215569)]
        data.reverse()

        chart_object.set_defaults(area.T,size=(xsiz,ysiz))

        myfs = fill_style.Plain(bgcolor=color.ivory1)

        # The attribute y_coord_system="category" tells that the Y axis values
        # should be taken from samples, y_category_col'th column of
        # y_category_data.  
        ar = area.T(y_coord = category_coord.T(data, 0),
                    x_grid_style=line_style.gray50_dash1,
                    x_grid_interval=5,
                    x_range = (-50,50), 
                    x_axis=axis.X(label=""),
                    y_grid_style=None,
                    y_axis=axis.Y(label=""),
                    y_axis2=axis.Y(offset=xsiz,draw_tics_right=1,label=""),
                    bg_style = myfs,
                    border_line_style = line_style.default,
                    legend = None)

        # Below call sets the default attributes for all bar plots.
        chart_object.set_defaults(bar_plot.T, direction="horizontal", data=data)

        #put together some fill styles with other colors as a test
        orange_solid = fill_style.Plain(bgcolor=color.orange)
        lightgoldenrod_solid = fill_style.Plain(bgcolor=color.lightgoldenrod)

        blst = []
        for q,r,s in data:
            z = 50 - s
            pl = bar_plot.T(data=[[q,z]],width=15,fill_style=fill_style.red)
            blst.append(pl)

        for x in blst:
            ar.add_plot(x)

        ar.draw(self.can)


    def draw_test2(self):
        xsiz = 150
        ysiz = 120

        theme.get_options()
        theme.use_color = True
        theme.reinitialize()

        data = [("Conceiving","Applying",52.9226328809),("Interacting","Contemplating",60.6060413003),
                ("Engaging","Distancing",44.6717376408),("Collaborating","Driving",47.1748466538),
                ("Adapting","Structuring",64.0713215569)]
        data.reverse()

        myfs = fill_style.Plain(bgcolor=color.ivory1)
        whitefs = fill_style.Plain(bgcolor=color.white)
        bluediag = fill_style.Rdiag(line_style=line_style.T(width=3,color=color.blue),line_interval=6)

        chart_object.set_defaults(area.T,size=(xsiz,ysiz))

        # The attribute y_coord_system="category" tells that the Y axis values
        # should be taken from samples, y_category_col'th column of
        # y_category_data.  
        ar = area.T(loc=(0,175),
                    y_coord = category_coord.T(data, 0),
                    x_grid_style=line_style.gray50_dash1,
                    x_grid_interval=5,
                    x_range = (-30,30), 
                    x_axis=axis.X(label=""),
                    y_grid_style=None,
                    y_axis=axis.Y(tic_label_offset=(-5,0),label=""),
                    bg_style = myfs,
                    border_line_style = line_style.default,
                    legend = None)

        ar2 = area.T(loc=(0,175),
                     y_coord = category_coord.T(data, 1),
                     x_axis=None,
                     y_grid_style=None,
                     y_axis=axis.Y(offset=xsiz,draw_tics_right=1,tic_label_offset=(5,0),label=""),
                     legend = None)

        # Below call sets the default attributes for all bar plots.
        chart_object.set_defaults(bar_plot.T,direction="horizontal",data=data)

        # setup the parameters for drawing the color range boxes
        xloc = ar.loc[0]
        ytip = ar.loc[1] + ar.size[1] #+ 15
        ybot = ar.loc[1] #- 20

        for q,r,s in data:
            z = (s - 50.0)
            pl = bar_plot.T(data=[[q,z,r]],width=10,fill_style=bluediag)
            ar.add_plot(pl)
            ar2.add_plot(pl)

        ar.draw(self.can)
        ar2.draw(self.can)

        # write over the flipping grid intervals on graph so that we can
        #  put in the unique text for the factor
        self.can.rectangle(None,whitefs,xloc-5,ybot-15,ar.x_pos(30)+5,ybot-1)
        #can.close()
        

# ----------------------------------------------------------------
# main program module
#
def main():
    s = summary_page()
    s.draw_test1()
    s.draw_test2()
    s.draw_can()


# ----------------------------------------------------------------
#  run main
#
if __name__ == "__main__": main()
