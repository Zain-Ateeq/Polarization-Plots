import plotly.graph_objs as go
import plotly.offline as py
import plotly

from ipywidgets import interactive, HBox, VBox, widgets, interact

import plotly.graph_objects as go
import math as m
import numpy as np

py.init_notebook_mode()

# load fig
fig = plotly.plotly.get_figure("https://plot.ly/~jordanpeterson/889")

# find the range of the slider.
xmin, xmax = fig['layout']['xaxis']['range']

# create FigureWidget from fig
f = go.FigureWidget(data=fig.data, layout=fig.layout)

slider = widgets.FloatRangeSlider(
    min=xmin,
    max=xmax,
    step=(xmax - xmin) / 1000.0,
    readout=False,
    description='Time')
slider.layout.width = '800px'


# our function that will modify the xaxis range
def update_range(y):
    f.layout.xaxis.range = [y[0], y[1]]


# display the FigureWidget and slider with center justification
vb = VBox((f, interactive(update_range, y=slider)))
vb.layout.align_items = 'center'
vb