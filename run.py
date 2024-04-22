import mesa
from rock_scissors_paper.model_original import RockScissorsPaperO
from rock_scissors_paper.portrayal import portraySquarePatch
from mesa.visualization import ChartModule, Slider, CanvasGrid, ModularServer

color_map = {
    0: 'red',
    1: 'purple',
    2: 'yellow'
}

model_params = {
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
     RockScissorsPaperO,
     [canvas_element, chart_element],
     "Rock Scissors Paper: Original",
     model_params
)
server.launch(open_browser=True)