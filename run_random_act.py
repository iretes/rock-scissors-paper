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
        "Initial weight of species 'rock'",
        0.33,
        0,
        1,
        0.01,
        description="Initial weight of species 'rock'",
    ),
    "s0": Slider(
        "Initial weight of species 'scissors'",
        0.33,
        0,
        1,
        0.01,
        description="Initial weight of species 'scissors'",
    ),
    "p0": Slider(
        "Initial weight of species 'paper'",
        0.33,
        0,
        1,
        0.01,
        description="Initial weight of species 'paper'",
    ),
    "Pr": Slider(
        "Invasion rate of species 'rock'",
        0.33,
        0,
        1,
        0.01,
        description="Invasion rate of species 'rock'",
    ),
    "Ps": Slider(
        "Invasion rate of species 'scissors'",
        0.33,
        0,
        1,
        0.01,
        description="Invasion rate of species 'scissors'",
    ),
    "Pp": Slider(
        "Invasion rate of species 'paper'",
        0.33,
        0,
        1,
        0.01,
        description="Invasion rate of species 'paper'",
    ),
    "color_map": color_map,
    "height": 100,
    "width": 100,
    "hex_grid": False
}

chart = []
for i in range(3):
    chart.append({'Label': i, 'Color': color_map[i]})
chart_element = ChartModule(chart, canvas_height=15, canvas_width=50)

canvas_element = CanvasGrid(
    portraySquarePatch,
    grid_width=100,
    grid_height=100,
    canvas_width=400,
    canvas_height=400
)

server = ModularServer(
     RockScissorsPaper,
     [canvas_element, chart_element],
     "Rock Scissors Paper (random activation of agents)",
     model_params
)
server.launch(open_browser=True)