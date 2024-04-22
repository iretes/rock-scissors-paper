import mesa
from mesa.visualization import Choice, ChartModule, Slider

color_map_SSR = {
    0: 'black',
    1: 'red',
    2: 'purple',
    3: 'yellow',
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
    "init0": Slider(
        "Initial weight of empty cells",
        0.25,
        0,
        1,
        0.01,
        description="Initial weight of empty cells",
    ),
    "init1": Slider(
        "Initial weight of species 1",
        0.25,
        0,
        1,
        0.01,
        description="Initial weight of species 1",
    ),
    "init2": Slider(
        "Initial weight of species 2",
        0.25,
        0,
        1,
        0.01,
        description="Initial weight of species 2",
    ),
    "init3": Slider(
        "Initial weight of species 3",
        0.25,
        0,
        1,
        0.01,
        description="Initial weight of species 3",
    ),
    "init4": Slider(
        "Initial weight of species 4",
        0,
        0,
        1,
        0.01,
        description="Initial weight of species 4",
    ),
    "init5": Slider(
        "Initial weight of species 5",
        0,
        0,
        1,
        0.01,
        description="Initial weight of species 5",
    ),
    "color_map": color_map_SSR
}

chart_SSR = []
for i in range(1, 6):
    chart_SSR.append({'Label': i, 'Color': color_map_SSR[i]})
chart_element_SSR = ChartModule(chart_SSR)