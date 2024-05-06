import mesa
from rock_scissors_paper.model_simultaneous_act import RockScissorsPaperSimultaneousActivation
from rock_scissors_paper.portrayal import portraySquarePatch
from mesa.visualization import ChartModule, Slider, CanvasGrid, ModularServer, Choice


color_map_simultaneous = {
    0: 'red',
    1: 'purple',
    2: 'yellow',
    3: 'green',
    4: 'blue'
}

model_params_simultaneous = {
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
    "color_map": color_map_simultaneous,
    "hex_grid": False,
    "height": 100,
    "width": 100,
}

chart = []
for i in range(5):
    chart.append({'Label': i, 'Color': color_map_simultaneous[i]})
chart_element_simultaneous = ChartModule(chart, canvas_height=15, canvas_width=50)

chart = []
for i in range(5):
    chart.append({'Label': i, 'Color': color_map_simultaneous[i]})
chart_element = ChartModule(chart, canvas_height=15, canvas_width=50)

canvas_element = CanvasGrid(
    portraySquarePatch,
    grid_width=100,
    grid_height=100,
    canvas_width=400,
    canvas_height=400
)

server = ModularServer(
     RockScissorsPaperSimultaneousActivation,
     [canvas_element, chart_element],
     "Rock Scissors Paper (simultaneaous activation of agents)",
     model_params_simultaneous
)
server.launch(open_browser=True)