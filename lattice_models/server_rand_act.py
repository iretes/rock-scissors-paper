import mesa
from mesa.visualization import Choice, ChartModule, Slider

color_map_randact = {
    0: 'red',
    1: 'purple',
    2: 'yellow',
    3: 'green',
    4: 'blue'
}

model_params_randact = {
    "n_species": Choice(
        "Number of species",
        value=3,
        choices=[3,4,5],
        description="Number of species"
    ),
    "init0": Slider(
        "Fraction of individuals of species 1",
        0.33,
        0,
        1,
        0.01,
        description="Fraction of individuals of species 1",
    ),
    "init1": Slider(
        "Fraction of individuals of species 2",
        0.33,
        0,
        1,
        0.01,
        description="Fraction of individuals of species 2",
    ),
    "init2": Slider(
        "Fraction of individuals of species 3",
        0.33,
        0,
        1,
        0.01,
        description="Fraction of individuals of species 3",
    ),
    "init3": Slider(
        "Fraction of individuals of species 4",
        0,
        0,
        1,
        0.01,
        description="Fraction of individuals of species 4",
    ),
    "init4": Slider(
        "Fraction of individuals of species 5",
        0,
        0,
        1,
        0.01,
        description="Fraction of individuals of species 5",
    ),
    "invrate0": Slider(
        "Invasion rate of species 1",
        0.33,
        0,
        1,
        0.01,
        description="Invasion rate of species 1",
    ),
    "invrate1": Slider(
        "Invasion rate of species 2",
        0.33,
        0,
        1,
        0.01,
        description="Invasion rate of species 2",
    ),
    "invrate2": Slider(
        "Invasion rate of species 3",
        0.33,
        0,
        1,
        0.01,
        description="Invasion rate of species 3",
    ),
    "invrate3": Slider(
        "Invasion rate of species 4",
        0.33,
        0,
        1,
        0.01,
        description="Invasion rate of species 4",
    ),
    "invrate4": Slider(
        "Invasion rate of species 5",
        0.33,
        0,
        1,
        0.01,
        description="Invasion rate of species 5",
    ),
    "color_map": color_map_randact
}

chart_randact = []
for i in range(5):
    chart_randact.append({'Label': i, 'Color': color_map_randact[i]})
chart_element_randact = ChartModule(chart_randact, canvas_height=15, canvas_width=50)