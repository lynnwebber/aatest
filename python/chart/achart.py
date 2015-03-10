#!/usr/bin/python
#
from pychart import *

theme.get_options()
theme.use_color = True
theme.output_format="png"
theme.output_file="charta.png"
theme.reinitialize()

#data = [("forcefullness",39.222),("confidence",28.97643),("sensitivity",49.8765),
#    ("rebelliousness",78.2826),("sociability",61.78923),("cooperativenss",53.2320981),
#    ("excitability",42.123456)]
#data.reverse()

#data = [("sample-26",26),("sample-36",36),("sample-46",46),
#    ("sample-51",51),("sample-56",56),("sample-66",66),
#    ("sample-76",76)]
#data.reverse()

data = [("Conceiving","Applying",52.9226328809),("Interacting","Contemplating",60.6060413003),
        ("Engaging","Distancing",44.6717376408),("Collaborating","Driving",47.1748466538),
        ("Adapting","Structuring",64.0713215569)]
data.reverse()

chart_object.set_defaults(area.T,size=(420,200))

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
            y_axis2=axis.Y(offset=420,draw_tics_right=1,label=""),
            bg_style = myfs,
            border_line_style = line_style.default,
            legend = None)

# Below call sets the default attributes for all bar plots.
chart_object.set_defaults(bar_plot.T, direction="horizontal", data=data)

#put together some fill styles with other colors as a test
orange_solid = fill_style.Plain(bgcolor=color.orange)
lightgoldenrod_solid = fill_style.Plain(bgcolor=color.lightgoldenrod)

#Less than or Equal to 30                           Red
#Greater than 30 and Less than or Equal to 40       Orange
#Greater than 40 and Less than or Equal to 47       Lightgoldenrod
#Greater than 47 and Less than 50                   Green
#Greater than or Equal to 50 and Less than 53       Green
#Greater than or Equal to 53 and Less than 60       Lightgoldenrod
#Greater than or Equal to 60 and Less than 70       Orange
#Greater than or Equal to 70                        Red


blst = []
for q,r,s in data:
    z = 50 - s
    pl = bar_plot.T(data=[[q,z]],width=15,fill_style=fill_style.red)
    blst.append(pl)

for x in blst:
    ar.add_plot(x)

ar.draw()

