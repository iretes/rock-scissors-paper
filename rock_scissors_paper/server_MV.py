import mesa
from mesa.visualization import Choice, ChartModule, Slider

color_map_MV = {
    0: 'red',
    1: 'purple',
    2: 'yellow',
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
    "init0": Slider(
        "Initial weight of species 1",
        0.33,
        0,
        1,
        0.01,
        description="Initial weight of species 1",
    ),
    "init1": Slider(
        "Initial weight of species 2",
        0.33,
        0,
        1,
        0.01,
        description="Initial weight of species 2",
    ),
    "init2": Slider(
        "Initial weight of species 3",
        0.33,
        0,
        1,
        0.01,
        description="Initial weight of species 3",
    ),
    "init3": Slider(
        "Initial weight of species 4",
        0,
        0,
        1,
        0.01,
        description="Initial weight of species 4",
    ),
    "init4": Slider(
        "Initial weight of species 5",
        0,
        0,
        1,
        0.01,
        description="Initial weight of species 5",
    ),
    "color_map": color_map_MV
}

chart = []
for i in range(5):
    chart.append({'Label': i, 'Color': color_map_MV[i]})
chart_element_MV = ChartModule(chart)