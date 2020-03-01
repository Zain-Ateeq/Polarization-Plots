from django.shortcuts import render
from .interface import WebInt
from plotly.offline import plot
import plotly.graph_objs as go
import math as m
import numpy as np


def old(request):
    # Request method
    if request.method == 'POST':
        interface = WebInt(request.POST)
        if interface.is_valid():
            select_an_option = interface.cleaned_data['select_an_option']
            select_the_plot = interface.cleaned_data['select_the_plot']
            slider = interface.cleaned_data['slider']

            # Fetching angle value from slider button
            y = slider[:-6]
            x = int(y)

            # Print to check submission
            print(select_an_option, select_the_plot, x)

            # Code for Polarizer 3
            if select_the_plot == 'P3 angle vs Unit Intensity':
                X = np.linspace(0, x, x + 1)
                Y = (2 + 2 * np.sin(2 * X * m.pi / 180) + 2 * pow(np.sin(X * m.pi / 180), 2)) / (4 * m.sqrt(2))
                trace1 = go.Scatter(x=X, y=Y, marker={'color': 'red', 'symbol': 104, 'size': 10},
                                    mode="lines", name='Unit Intensity Curve')
                data = go.Data([trace1])
                layout = go.Layout(title="Polarizer Angle vs Unit Intensity",
                                   xaxis={'title': 'Polarizer Angle (Degrees)'},
                                   yaxis={'title': 'Unit Intensity (W/m^2)'})
                figure = go.Figure(data=data, layout=layout)
                plot_div = plot(figure, auto_open=True, output_type='div')
                return render(request, 'p3plot.html', context={'plot_div': plot_div})

            # Code for Polarizer 4
            if select_the_plot == 'P4 angle vs Unit Intensity':
                X = np.linspace(0, x, x + 1)
                Y = (1 + 2 * np.sin(X * m.pi / 180) * np.cos(X * m.pi / 180)) / 2
                trace1 = go.Scatter(x=X, y=Y, marker={'color': 'red', 'symbol': 104, 'size': 10},
                                    mode="lines", name='Unit Intensity Curve')
                data = go.Data([trace1])
                layout = go.Layout(title="Polarizer Angle vs Unit Intensity",
                                   xaxis={'title': 'Polarizer Angle (Degrees)'},
                                   yaxis={'title': 'Unit Intensity (W/m^2)'})
                figure = go.Figure(data=data, layout=layout)
                plot_div = plot(figure, auto_open=True, output_type='div')
                return render(request, 'p4plot.html', context={'plot_div': plot_div})

            # Code for Quarter wave plate
            if select_the_plot == 'QWP angle vs Unit Intensity':
                X = np.linspace(0, x, x + 1)
                Y = pow(np.cos(X * m.pi / 180), 2)
                trace1 = go.Scatter(x=X, y=Y, marker={'color': 'red', 'symbol': 104, 'size': 10},
                                    mode="lines", name='Unit Intensity Curve')
                data = go.Data([trace1])
                layout = go.Layout(title="QWP Angle vs Unit Intensity",
                                   xaxis={'title': 'Quarter Wave Plate Angle (Degrees)'},
                                   yaxis={'title': 'Unit Intensity (W/m^2)'})
                figure = go.Figure(data=data, layout=layout)
                plot_div = plot(figure, auto_open=True, output_type='div')
                return render(request, 'qwpplot.html', context={'plot_div': plot_div})

            # Code for Half wave plate
            if select_the_plot == 'HWP angle vs Unit Intensity':

                # When 'Overlap' is selected in radio button
                if select_an_option == 'overlap':
                    X = np.linspace(0, x, x + 1)
                    Y1 = pow(np.cos(X * 2 * m.pi / 180), 2)
                    Y2 = pow(np.sin(X * 2 * m.pi / 180), 2)

                    # Intensity parameters at detector B
                    trace1 = go.Scatter(x=X, y=Y1, marker={'color': 'red', 'symbol': 104, 'size': 10},
                                        mode="lines", name='Detector B')
                    # Intensity parameters at detector A
                    trace2 = go.Scatter(x=X, y=Y2, marker={'color': 'green', 'symbol': 104, 'size': 10},
                                        mode="lines", name='Detector A')
                    data = go.Data([trace1, trace2])
                    layout = go.Layout(title="Half Wave Plate Angle vs Unit Intensity",
                                       xaxis={'title': 'Polarizer Angle (Degrees)'},
                                       yaxis={'title': 'Unit Intensity (W/m^2)'})
                    figure = go.Figure(data=data, layout=layout)
                    plot_div = plot(figure, auto_open=True, output_type='div')
                    return render(request, 'hwpplot.html', context={'plot_div': plot_div})

                # When 'Separate' is selected in radio button
                else:
                    X = np.linspace(0, x, x + 1)
                    Y1 = pow(np.cos(X * 2 * m.pi / 180), 2)
                    Y2 = pow(np.sin(X * 2 * m.pi / 180), 2)

                    # Intensity parameters at detector B
                    plot_div1 = go.Scatter(x=X, y=Y1, marker={'color': 'red', 'symbol': 104, 'size': 10},
                                           mode="lines", name='Detector B')
                    # Intensity parameters at detector A
                    plot_div2 = go.Scatter(x=X, y=Y2, yaxis="y2", marker={'color': 'green', 'symbol': 104, 'size': 10},
                                           mode="lines", name='Detector A')

                    data = go.Data([plot_div1, plot_div2])
                    layout = go.Layout(title="Half Wave Plate Angle vs Unit Intensity",
                                       xaxis={'title': 'Quarter Wave Plate Angle (Degrees)'},
                                       yaxis={'title': 'Unit Intensity (W/m^2)'},
                                       yaxis1=dict(domain=[0, 0.50]), legend=dict(traceorder="reversed"),
                                       yaxis2=dict(domain=[0.50, 1.00]),
                                       )
                    figure = go.Figure(data=data, layout=layout)
                    fig = plot(figure, auto_open=True, output_type='div')
                    return render(request, 'paplot.html', context={'plot_div': fig})

            # Code for Polarizer
            if select_the_plot == 'Polarizer angle vs Unit Intensity':

                # When 'Overlap' is selected in radio button
                if select_an_option == 'overlap':
                    X = np.linspace(0, x, x + 1)
                    Y1 = pow(np.cos(X * m.pi / 180), 2)
                    Y2 = pow(np.sin(X * m.pi / 180), 2)

                    # Intensity parameters at detector B
                    trace1 = go.Scatter(x=X, y=Y1, marker={'color': 'red', 'symbol': 104, 'size': 10},
                                        mode="lines", name='Detector B')
                    # Intensity parameters at detector B
                    trace2 = go.Scatter(x=X, y=Y2, marker={'color': 'green', 'symbol': 104, 'size': 10},
                                        mode="lines", name='Detector A')

                    data = go.Data([trace1, trace2])
                    layout = go.Layout(title="Polarizer Angle vs Unit Intensity",
                                       xaxis={'title': 'Polarizer Angle (Degrees)'},
                                       yaxis={'title': 'Unit Intensity (W/m^2)'})
                    figure = go.Figure(data=data, layout=layout)
                    plot_div = plot(figure, auto_open=True, output_type='div')
                    return render(request, 'paplot.html', context={'plot_div': plot_div})

                # When 'Separate' is selected in radio button
                else:
                    X = np.linspace(0, x, x + 1)
                    Y1 = pow(np.cos(X * m.pi / 180), 2)
                    Y2 = pow(np.sin(X * m.pi / 180), 2)

                    # Intensity parameters at detector B
                    plot_div1 = go.Scatter(x=X, y=Y1, marker={'color': 'red', 'symbol': 104, 'size': 10},
                                           mode="lines", name='Detector B')
                    # Intensity parameters at detector A
                    plot_div2 = go.Scatter(x=X, y=Y2, yaxis="y2", marker={'color': 'green', 'symbol': 104, 'size': 10},
                                           mode="lines", name='Detector A')

                    data = go.Data([plot_div1, plot_div2])
                    layout = go.Layout(title="Polarizer Angle vs Unit Intensity",
                                       xaxis={'title': 'Polarizer Angle (Degrees)'},
                                       yaxis1=dict(domain=[0, 0.50]), legend=dict(traceorder="reversed"),
                                       yaxis2=dict(domain=[0.50, 1.00]), yaxis={'title': 'Unit Intensity (W/m^2)'},
                                       )
                    figure = go.Figure(data=data, layout=layout)
                    fig = plot(figure, auto_open=True, output_type='div')
                    return render(request, 'paplot.html', context={'plot_div': fig})

    interface = WebInt()
    return render(request, 'interface.html', {'interface': interface})


def about(request):
    fig = go.Figure()

    # Add traces, one for each slider step
    for step in np.arange(0, 36.10, 0.10):
        x = step * np.arange(0, 10.00, 0.01)

        fig.add_trace(
            go.Scatter(
                visible=False,
                line=dict(color="#00CED1", width=6),
                name="𝜈 = " + str(step),
                x=x,
                y=(2 + 2 * np.sin(2 * x * m.pi / 180.00) + 2 * pow(np.sin(x * m.pi / 180.00), 2)) / (4 * m.sqrt(2))
            ))

    # Make 10th trace visible

    fig.data[360].visible = True

    # Create and add slider
    steps = []
    for i in range(len(fig.data)):
        step = dict(
            method="restyle",
            args=["visible", [False] * len(fig.data)],
        )
        step["args"][1][i] = True  # Toggle i'th trace to "visible"
        steps.append(step)

    sliders = [dict(
        active=360,
        currentvalue={"prefix": "Frequency: "},
        pad={"t": 50},
        steps=steps
    )]

    fig.update_layout(
        sliders=sliders
    )

    plot_div = plot(fig, auto_open=True, output_type='div')
    return render(request, 'p3plot.html', context={'plot_div': plot_div})


def home(request):
    x = np.linspace(0, 360, 361)

    # Initialize figure
    fig = go.Figure()

    # Add Traces

    # Polarizer 3
    fig.add_trace(
        go.Scatter(x=x,
                   y=(2 + 2 * np.sin(2 * x * m.pi / 180) + 2 * pow(np.sin(x * m.pi / 180), 2)) / (4 * m.sqrt(2)),
                   name="P3 Plot",
                   visible=False,
                   line=dict(color="#d62728")))

    # Polarizer 4
    fig.add_trace(
        go.Scatter(x=x,
                   y=(1 + 2 * np.sin(x * m.pi / 180) * np.cos(x * m.pi / 180)) / 2,
                   name="P4 Plot",
                   visible=False,
                   line=dict(color="#33CFA5")))

    # Quarter Wave Plate
    fig.add_trace(
        go.Scatter(x=x,
                   y=pow(np.cos(x * m.pi / 180), 2),
                   name="QWP Plot",
                   visible=False,
                   line=dict(color="#1f77b4")))

    # Half Wave Plate 1
    fig.add_trace(
        go.Scatter(x=x,
                   y=pow(np.cos(x * 2 * m.pi / 180), 2),
                   name="HWP Detector A Plot",
                   visible=False,
                   line=dict(color="#bcbd22")))

    # Half Wave Plate 2
    fig.add_trace(
        go.Scatter(x=x,
                   y=pow(np.sin(x * 2 * m.pi / 180), 2),
                   name="HWP Detector B Plot",
                   visible=False,
                   line=dict(color="#7f7f7f")))

    # Main Polarizer 1
    fig.add_trace(
        go.Scatter(x=x,
                   y=pow(np.cos(x * m.pi / 180), 2),
                   name="P Detector A Plot",
                   visible=False,
                   line=dict(color="#9467bd")))

    # Main Polarizer 2
    fig.add_trace(
        go.Scatter(x=x,
                   y=pow(np.sin(x * m.pi / 180), 2),
                   name="P Detector B Plot",
                   visible=False,
                   line=dict(color="#ff7f0e")))

    fig.update_layout(
        yaxis={'title': 'Unit Intensity (W/m^2)'},
        xaxis=dict(
            rangeselector=dict(

            ),
            rangeslider=dict(
                visible=True
            )
        ),
        updatemenus=[
            dict(
                active=0,
                buttons=list([
                    dict(label="None",
                         method="update",
                         args=[{"visible": [False, False, False, False, False, False, False]},
                               {"title": "Select any plot from drop down menu"}]),
                    dict(label="P3 Plot",
                         method="update",
                         args=[{"visible": [True, False, False, False, False, False, False]},
                               {"title": "Polarizer 3 vs Unit Intensity"}]),
                    dict(label="P4 Plot",
                         method="update",
                         args=[{"visible": [False, True, False, False, False, False, False]},
                               {"title": "Polarizer 4 vs Unit Intensity"}]),
                    dict(label="QWP Plot",
                         method="update",
                         args=[{"visible": [False, False, True, False, False, False, False]},
                               {"title": "QWP vs Unit Intensity"}]),
                    dict(label="HWP Plot",
                         method="update",
                         args=[{"visible": [False, False, False, True, True, False, False]},
                               {"title": "HWP vs Unit Intensity"}]),
                    dict(label="P Plot",
                         method="update",
                         args=[{"visible": [False, False, False, False, False, True, True]},
                               {"title": "Polarizer vs Unit Intensity"}]),
                    dict(label="All",
                         method="update",
                         args=[{"visible": [True, True, True, True, True, True, True]},
                               {"title": "Overlapped Plots"}])
                ]),
            )
        ],
    )

    # Set title
    fig.update_layout(title_text="Select any plot from drop down menu")
    plot_div = plot(fig, auto_open=True, output_type='div')
    return render(request, 'home.html', context={'plot_div': plot_div})
