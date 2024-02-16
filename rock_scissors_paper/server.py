import mesa
from .model import RockScissorsPaper
from .portrayal import portraySquarePatch, portrayHexPatch
from mesa.visualization import CanvasHexGrid, CanvasGrid, StaticText, Choice, ChartModule, Slider, ModularServer

grid_width = 50
grid_height = 50
hex_canvas_element = CanvasHexGrid(
    portrayHexPatch,
    grid_width=grid_width,
    grid_height=grid_height,
    canvas_width=500,
    canvas_height=500
) 
square_canvas_element = CanvasGrid(
    portraySquarePatch,
    grid_width=grid_width,
    grid_height=grid_height,
    canvas_width=500,
    canvas_height=500
)

rules_descr = '<b>Rules with 3 species:</b><br />'
for key, val in RockScissorsPaper.rules3.items():
    rules_descr += f'{key} > {val[0]}<br />'
rules_descr += '<b>Rules with 4 species:</b><br />'
for key, val in RockScissorsPaper.rules4.items():
    rules_descr += f'{key} > {val[0]}<br />'
rules_descr += '(<0,2> and <1,3> do not compete)<br />'
rules_descr += '<b>Rules with 5 species:</b><br />'
for key, val in RockScissorsPaper.rules5.items():
    rules_descr += f'{key} > {val[0]}, {val[1]}<br />'

color_map = {
    0: 'red',
    1: 'yellow',
    2: 'purple',
    3: 'green',
    4: 'blue'
}

model_params = {
    "height": grid_height,
    "width": grid_width,
    "rules_descr": StaticText(rules_descr),
    "n_species": Choice(
        "Number of species",
        value=3,
        choices=[3,4,5],
        description="Number of species"
    ),
    "prob0": Slider(
        "Fraction of individuals of species 0",
        0.33,
        0,
        1,
        0.01,
        description="Fraction of individuals of species 0",
    ),
    "prob1": Slider(
        "Fraction of individuals of species 1",
        0.33,
        0,
        1,
        0.01,
        description="Fraction of individuals of species 1",
    ),
    "prob2": Slider(
        "Fraction of individuals of species 2",
        0.33,
        0,
        1,
        0.01,
        description="Fraction of individuals of species 2",
    ),
    "prob3": Slider(
        "Fraction of individuals of species 3",
        0,
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
    "color_map": color_map
}

chart = []
for i in range(5):
    chart.append({'Label': i, 'Color': color_map[i]})
chart_element = ChartModule(chart)

hex_model_params = model_params.copy()
hex_model_params['hex'] = True
hex_server = ModularServer(
    RockScissorsPaper, [hex_canvas_element, chart_element], "Rock Scissors Paper", hex_model_params
)

square_model_params = model_params.copy()
square_model_params['hex'] = False
square_server = ModularServer(
    RockScissorsPaper, [square_canvas_element, chart_element], "Rock Scissors Paper", square_model_params
)