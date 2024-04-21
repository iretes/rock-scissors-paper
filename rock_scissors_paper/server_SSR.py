import mesa
from mesa.visualization import Choice, ChartModule, Slider

color_map_SSR = {
    0: 'black',
    1: 'red',
    2: 'yellow',
    3: 'purple',
    4: 'green',
    5: 'blue'
}

model_params_SSR = {
    "n_species": Choice(
        "Number of species",
        value=3,
        choices=[3,4,5],
        description="Number of species"
    ),
    "prob0": Slider(
        "Fraction of empty patches",
        0.25,
        0,
        1,
        0.01,
        description="Fraction of empty patches",
    ),
    "prob1": Slider(
        "Fraction of individuals of species 1",
        0.25,
        0,
        1,
        0.01,
        description="Fraction of individuals of species 1",
    ),
    "prob2": Slider(
        "Fraction of individuals of species 2",
        0.25,
        0,
        1,
        0.01,
        description="Fraction of individuals of species 2",
    ),
    "prob3": Slider(
        "Fraction of individuals of species 3",
        0.25,
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
    "prob5": Slider(
        "Fraction of individuals of species 5",
        0,
        0,
        1,
        0.01,
        description="Fraction of individuals of species 5",
    ),
    "color_map": color_map_SSR
}

chart_SSR = []
for i in range(1, 6):
    chart_SSR.append({'Label': i, 'Color': color_map_SSR[i]})
chart_element_SSR = ChartModule(chart_SSR)