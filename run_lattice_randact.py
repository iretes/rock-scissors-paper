import mesa
from lattice_models.model_rand_act import RSPRandAct
from lattice_models.portrayal import portraySquarePatch
from mesa.visualization import Choice, ChartModule, Slider, CanvasGrid, ModularServer, StaticText

color_map = {
    0: 'red',
    1: 'purple',
    2: 'yellow',
    3: 'green',
    4: 'blue'
}

model_params = {
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
    "invrate0": Slider(
        "Invasion rate of species 1",
        0.33,
        0,
        1,
        0.01,
        description="Invasion rate of species 1",
    ),
    "invrate1": Slider(
        "Invasion rate of species species 2",
        0.33,
        0,
        1,
        0.01,
        description="Invasion rate of species 2",
    ),
    "invrate2": Slider(
        "Invasion rate of species of species 3",
        0.33,
        0,
        1,
        0.01,
        description="Invasion rate of species 3",
    ),
    "invrate3": Slider(
        "Invasion rate of species of species 4",
        0,
        0,
        1,
        0.01,
        description="Invasion rate of species 4",
    ),
    "invrate4": Slider(
        "Invasion rate of species of species 5",
        0,
        0,
        1,
        0.01,
        description="Invasion rate of species 5",
    ),
    "color_map": color_map,
    "height": 100,
    "width": 100
}

chart = []
for i in range(5):
    chart.append({'Label': i, 'Color': color_map[i]})
chart_element = ChartModule(chart, canvas_height=15, canvas_width=50)

canvas_element = CanvasGrid(
    portraySquarePatch,
    grid_width=100,
    grid_height=100,
    canvas_width=400,
    canvas_height=400
)

rules_descr = '<b>Rules with 3 species:</b><br />'
for key, val in RSPRandAct.rules3.items():
    rules_descr += f'{key} > {val[0]}<br />'
rules_descr += '<b>Rules with 4 species:</b><br />'
for key, val in RSPRandAct.rules4.items():
    rules_descr += f'{key} > {val[0]}<br />'
rules_descr += '(<2,4> and <1,3> do not compete)<br />'
rules_descr += '<b>Rules with 5 species:</b><br />'
for key, val in RSPRandAct.rules5.items():
    rules_descr += f'{key} > {val[0]}, {val[1]}<br />'

model_params['rules_descr'] = StaticText(rules_descr)

server = ModularServer(
     RSPRandAct,
     [canvas_element, chart_element],
     "Rock Scissors Paper (random activation of agents)",
     model_params
)
server.launch(open_browser=True)