import mesa
from mesa.visualization import Choice, ChartModule, Slider

color_map = {
    0: 'red',
    1: 'purple',
    2: 'yellow'
}

model_params = {
    "r0": Slider(
        "Fraction of individuals of species 1",
        0.33,
        0,
        1,
        0.01,
        description="Fraction of individuals of species 1",
    ),
    "s0": Slider(
        "Fraction of individuals of species 2",
        0.33,
        0,
        1,
        0.01,
        description="Fraction of individuals of species 2",
    ),
    "p0": Slider(
        "Fraction of individuals of species 3",
        0.33,
        0,
        1,
        0.01,
        description="Fraction of individuals of species 3",
    ),
    "Pr": Slider(
        "Invasion rate of species 1",
        0.33,
        0,
        1,
        0.01,
        description="Invasion rate of species 1",
    ),
    "Ps": Slider(
        "Invasion rate of species 2",
        0.33,
        0,
        1,
        0.01,
        description="Invasion rate of species 2",
    ),
    "Pp": Slider(
        "Invasion rate of species 3",
        0.33,
        0,
        1,
        0.01,
        description="Invasion rate of species 3",
    ),
    "color_map": color_map
}

chart = []
for i in range(3):
    chart.append({'Label': i, 'Color': color_map[i]})
chart_element = ChartModule(chart, canvas_height=15, canvas_width=50)