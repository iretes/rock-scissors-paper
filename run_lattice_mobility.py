import mesa
from lattice_models.model_mobility import RSPMobility
from lattice_models.portrayal import portraySquarePatch
from mesa.visualization import ChartModule, Slider, CanvasGrid, ModularServer, Choice, StaticText

color_map = {
    0: 'black',
    1: 'red',
    2: 'purple',
    3: 'yellow',
    4: 'green',
    5: 'blue'
}

model_params = {
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
    "swap_exp": Slider(
        "Swap rate",
        0,
        -1,
        1,
        0.01,
        description="Swap exponent",
    ),
    "reproduce_exp": Slider(
        "Reproduce rate",
        0,
        -1,
        1,
        0.01,
        description="Reproduce exponent",
    ),
    "select_exp": Slider(
        "Select rate",
        0,
        -1,
        1,
        0.01,
        description="Select exponent",
    ),
    "color_map": color_map,
    "height": 100,
    "width": 100
}

chart_mobility = []
for i in range(1, 6):
    chart_mobility.append({'Label': i, 'Color': color_map[i]})
chart_element_mobility = ChartModule(chart_mobility, canvas_height=15, canvas_width=50)

canvas_element = CanvasGrid(
    portraySquarePatch,
    grid_width=100,
    grid_height=100,
    canvas_width=400,
    canvas_height=400
)

rules_descr = '<b>Rules with 3 species:</b><br />'
for key, val in RSPMobility.rules3.items():
    rules_descr += f'{key} > {val[0]}<br />'
rules_descr += '<b>Rules with 4 species:</b><br />'
for key, val in RSPMobility.rules4.items():
    rules_descr += f'{key} > {val[0]}<br />'
rules_descr += '(<0,2> and <1,3> do not compete)<br />'
rules_descr += '<b>Rules with 5 species:</b><br />'
for key, val in RSPMobility.rules5.items():
    rules_descr += f'{key} > {val[0]}, {val[1]}<br />'

model_params['rules_descr'] = StaticText(rules_descr)

server = ModularServer(
     RSPMobility,
     [canvas_element, chart_element_mobility],
     "Rock Scissors Paper (mobility)",
     model_params
)
server.launch(open_browser=True)