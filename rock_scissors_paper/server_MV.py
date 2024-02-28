import mesa
from mesa.visualization import Choice, ChartModule, Slider

color_map_MV = {
    0: 'red',
    1: 'yellow',
    2: 'purple',
    3: 'green',
    4: 'blue'
}

model_params_MV = {
    "n_species": Choice(
        "Number of species",
        value=3,
        choices=[3,4,5],
        description="Number of species"
    ),
    "prob0": Slider(
        "Fraction of individuals of species 0",
        0.33,
        0,
        1,
        0.01,
        description="Fraction of individuals of species 0",
    ),
    "prob1": Slider(
        "Fraction of individuals of species 1",
        0.33,
        0,
        1,
        0.01,
        description="Fraction of individuals of species 1",
    ),
    "prob2": Slider(
        "Fraction of individuals of species 2",
        0.33,
        0,
        1,
        0.01,
        description="Fraction of individuals of species 2",
    ),
    "prob3": Slider(
        "Fraction of individuals of species 3",
        0,
        0,
        1,
        0.01,
        description="Fraction of individuals of species 3",
    ),
    "prob4": Slider(
        "Fraction of individuals of species 4",
        0,
        0,
        1,
        0.01,
        description="Fraction of individuals of species 4",
    ),
    "color_map": color_map_MV
}

chart = []
for i in range(5):
    chart.append({'Label': i, 'Color': color_map_MV[i]})
chart_element_MV = ChartModule(chart)