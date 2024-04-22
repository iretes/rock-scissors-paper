import mesa
from mesa.visualization import Choice, ChartModule, Slider

color_map_O = {
    0: 'red',
    1: 'purple',
    2: 'yellow'
}

model_params_O = {
    "prob0": Slider(
        "Fraction of individuals of species 1",
        0.33,
        0,
        1,
        0.01,
        description="Fraction of individuals of species 1",
    ),
    "prob1": Slider(
        "Fraction of individuals of species 2",
        0.33,
        0,
        1,
        0.01,
        description="Fraction of individuals of species 2",
    ),
    "prob2": Slider(
        "Fraction of individuals of species 3",
        0.33,
        0,
        1,
        0.01,
        description="Fraction of individuals of species 3",
    ),
    "inv0": Slider(
        "Invasion rate of species 1",
        0.33,
        0,
        1,
        0.01,
        description="Invasion rate of species 1",
    ),
    "inv1": Slider(
        "Invasion rate of species 2",
        0.33,
        0,
        1,
        0.01,
        description="Invasion rate of species 2",
    ),
    "inv2": Slider(
        "Invasion rate of species 3",
        0.33,
        0,
        1,
        0.01,
        description="Invasion rate of species 3",
    ),
    "color_map": color_map_O
}

chart_O = []
for i in range(3):
    chart_O.append({'Label': i, 'Color': color_map_O[i]})
chart_element_O = ChartModule(chart_O)