import mesa
from rock_scissors_paper.model_random_act import RockScissorsPaper
from rock_scissors_paper.portrayal import portraySquarePatch
from mesa.visualization import ChartModule, Slider, CanvasGrid, ModularServer

color_map = {
    0: 'red',
    1: 'purple',
    2: 'yellow'
}

model_params = {
    "r0": Slider(
        "Initial weight of species 1",
        0.33,
        0,
        1,
        0.01,
        description="Initial weight of species 1",
    ),
    "s0": Slider(
        "Initial weight of species 2",
        0.33,
        0,
        1,
        0.01,
        description="Initial weight of species 2",
    ),
    "p0": Slider(
        "Initial weight of species 3",
        0.33,
        0,
        1,
        0.01,
        description="Initial weight of species 3",
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
    "color_map": color_map,
    "height": 200,
    "width": 200,
    "hex": False
}

chart = []
for i in range(3):
    chart.append({'Label': i, 'Color': color_map[i]})
chart_element = ChartModule(chart)

canvas_element = CanvasGrid(
    portraySquarePatch,
    grid_width=200,
    grid_height=200,
    canvas_width=600,
    canvas_height=600
)

server = ModularServer(
     RockScissorsPaper,
     [canvas_element, chart_element],
     "Rock Scissors Paper (random activation of agents)",
     model_params
)
server.launch(open_browser=True)