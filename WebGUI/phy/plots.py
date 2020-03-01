from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.graph_objects as go
import math as m
import numpy as np

# django-matplotlib
from django.db import models
from django_matplotlib.fields import MatplotlibFigureField
import matplotlib.pyplot as plt


def p3plot(request):
    X = np.linspace(0, 360, 361)
    Y = (2 + 2 * np.sin(2 * X * m.pi / 180) + 2 * pow(np.sin(X * m.pi / 180), 2)) / (4 * m.sqrt(2))
    plot_div = plot([Scatter(x=X, y=Y,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    return render(request, "p3plot.html", context={'plot_div': plot_div})


def p4plot(request):
    X = np.linspace(0, 360, 361)
    Y = (1 + 2 * np.sin(X * m.pi / 180) * np.cos(X * m.pi / 180)) / 2
    plot_div = plot([Scatter(x=X, y=Y,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    return render(request, "p4plot.html", context={'plot_div': plot_div})


def qwpplot(request):
    X = np.linspace(0, 360, 361)
    Y = pow(np.cos(X * m.pi / 180), 2)
    plot_div = plot([Scatter(x=X, y=Y,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    return render(request, "qwpplot.html", context={'plot_div': plot_div})


def hwpplot(request):
    X = np.linspace(0, 360, 361)
    i = X % 2
    Y1 = pow(np.cos(X * 2 * m.pi / 180), 2)
    Y2 = pow(np.sin(X * 2 * m.pi / 180), 2)
    plot_div1 = go.Scatter(
        x=X,
        y=Y1,
    )
    plot_div2 = go.Scatter(
        x=X,
        y=Y2,
        yaxis="y2"
    )
    data = [plot_div1, plot_div2]
    layout = go.Layout(
        yaxis=dict(
            domain=[0, 0.33]
        ),
        legend=dict(
            traceorder="reversed"
        ),
        yaxis2=dict(
            domain=[0.33, 0.66]
        ),
        yaxis3=dict(
            domain=[0.66, 1]
        )
    )
    fig = go.Figure(data=data, layout=layout)
    fig.show()
    return render(request, "hwpplot.html", context={'plot_div': fig})


def paplot(request):
    X = np.linspace(0, 360, 361)
    i = X % 2
    Y1 = pow(np.cos(X * m.pi / 180), 2)
    Y2 = pow(np.sin(X * m.pi / 180), 2)
    plot_div1 = go.Scatter(
        x=X,
        y=Y1,
    )
    plot_div2 = go.Scatter(
        x=X,
        y=Y2,
        yaxis="y2"
    )
    data = [plot_div1, plot_div2]
    layout = go.Layout(
        yaxis=dict(
            domain=[0, 0.33]
        ),
        legend=dict(
            traceorder="reversed"
        ),
        yaxis2=dict(
            domain=[0.33, 0.66]
        ),
        yaxis3=dict(
            domain=[0.66, 1]
        )
    )
    fig = go.Figure(data=data, layout=layout)
    fig.show()
    return render(request, "paplot.html", context={'plot_div': fig})

def hwpplot(request):
    x = np.linspace(0, 360, 361)
    y1 = pow(np.cos(x * 2 * (m.pi) / 180), 2)
    y2 = pow(np.sin(x * 2 * (m.pi) / 180), 2)
    plt.plot(x, y1, label='Detector B (V)')
    plt.plot(x, y2, label='Detector A (H)')
    plt.legend()
    plt.xlabel('HWP Angle (degrees)')
    plt.ylabel('Intensity (W/m^2)')
    plt.title('Half Wave Plate Angle vs Intensity Plot')
    plt.show()

    # Load dataset
    df = pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")
    df.columns = [col.replace("AAPL.", "") for col in df.columns]

    # Initialize figure
    fig = go.Figure()

    # Add Traces

    fig.add_trace(
        go.Scatter(x=list(df.index),
                   y=list(df.High),
                   name="High",
                   line=dict(color="#33CFA5")))

    fig.add_trace(
        go.Scatter(x=list(df.index),
                   y=[df.High.mean()] * len(df.index),
                   name="High Average",
                   visible=False,
                   line=dict(color="#33CFA5", dash="dash")))

    fig.add_trace(
        go.Scatter(x=list(df.index),
                   y=list(df.Low),
                   name="Low",
                   line=dict(color="#F06A6A")))

    fig.add_trace(
        go.Scatter(x=list(df.index),
                   y=[df.Low.mean()] * len(df.index),
                   name="Low Average",
                   visible=False,
                   line=dict(color="#F06A6A", dash="dash")))

    # Add Annotations and Buttons
    high_annotations = [dict(x="2016-03-01",
                             y=df.High.mean(),
                             xref="x", yref="y",
                             text="High Average:<br> %.3f" % df.High.mean(),
                             ax=0, ay=-40),
                        dict(x=df.High.idxmax(),
                             y=df.High.max(),
                             xref="x", yref="y",
                             text="High Max:<br> %.3f" % df.High.max(),
                             ax=0, ay=-40)]
    low_annotations = [dict(x="2015-05-01",
                            y=df.Low.mean(),
                            xref="x", yref="y",
                            text="Low Average:<br> %.3f" % df.Low.mean(),
                            ax=0, ay=40),
                       dict(x=df.High.idxmin(),
                            y=df.Low.min(),
                            xref="x", yref="y",
                            text="Low Min:<br> %.3f" % df.Low.min(),
                            ax=0, ay=40)]

    fig.update_layout(
        updatemenus=[
            dict(
                active=0,
                buttons=list([
                    dict(label="None",
                         method="update",
                         args=[{"visible": [True, False, True, False]},
                               {"title": "Yahoo",
                                "annotations": []}]),
                    dict(label="High",
                         method="update",
                         args=[{"visible": [True, True, False, False]},
                               {"title": "Yahoo High",
                                "annotations": high_annotations}]),
                    dict(label="Low",
                         method="update",
                         args=[{"visible": [False, False, True, True]},
                               {"title": "Yahoo Low",
                                "annotations": low_annotations}]),
                    dict(label="Both",
                         method="update",
                         args=[{"visible": [True, True, True, True]},
                               {"title": "Yahoo",
                                "annotations": high_annotations + low_annotations}]),
                ]),
            )
        ])

    # Set title
    fig.update_layout(title_text="Yahoo")

    import plotly.graph_objects as go
    import numpy as np

    # Create figure
    fig = go.Figure()

    # Add traces, one for each slider step
    for step in np.arange(0, 5, 0.1):
        fig.add_trace(
            go.Scatter(
                visible=False,
                line=dict(color="#00CED1", width=6),
                name="𝜈 = " + str(step),
                x=np.arange(0, 10, 0.01),
                y=np.sin(step * np.arange(0, 10, 0.01))))

    # Make 10th trace visible
    fig.data[10].visible = True

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
        active=10,
        currentvalue={"prefix": "Frequency: "},
        pad={"t": 50},
        steps=steps
    )]

    fig.update_layout(
        sliders=sliders
    )

    fig.show()


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