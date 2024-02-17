import mesa
from .model_empty import RockScissorsPaperEmpty
from .portrayal import portraySquarePatch, portrayHexPatch
from mesa.visualization import CanvasHexGrid, CanvasGrid, StaticText, Choice, ChartModule, Slider, ModularServer

grid_width = 150
grid_height = 150
hex_canvas_element = CanvasHexGrid(
    portrayHexPatch,
    grid_width=grid_width,
    grid_height=grid_height,
    canvas_width=450,
    canvas_height=450
) 
square_canvas_element = CanvasGrid(
    portraySquarePatch,
    grid_width=grid_width,
    grid_height=grid_height,
    canvas_width=450,
    canvas_height=450
)

rules_descr = '<b>Rules with 3 species:</b><br />'
for key, val in RockScissorsPaperEmpty.rules3.items():
    rules_descr += f'{key} > {val[0]}<br />'
rules_descr += '<b>Rules with 4 species:</b><br />'
for key, val in RockScissorsPaperEmpty.rules4.items():
    rules_descr += f'{key} > {val[0]}<br />'
rules_descr += '(<0,2> and <1,3> do not compete)<br />'
rules_descr += '<b>Rules with 5 species:</b><br />'
for key, val in RockScissorsPaperEmpty.rules5.items():
    rules_descr += f'{key} > {val[0]}, {val[1]}<br />'

color_map = {
    0: 'black',
    1: 'red',
    2: 'yellow',
    3: 'purple',
    4: 'green',
    5: 'blue'
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
        0.25,
        0,
        1,
        0.01,
        description="Fraction of empty patches",
    ),
    "prob1": Slider(
        "Fraction of individuals of species 1",
        0.25,
        0,
        1,
        0.01,
        description="Fraction of individuals of species 1",
    ),
    "prob2": Slider(
        "Fraction of individuals of species 2",
        0.25,
        0,
        1,
        0.01,
        description="Fraction of individuals of species 2",
    ),
    "prob3": Slider(
        "Fraction of individuals of species 3",
        0.25,
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
    "prob5": Slider(
        "Fraction of individuals of species 5",
        0,
        0,
        1,
        0.01,
        description="Fraction of individuals of species 5",
    ),
    "color_map": color_map
}

chart = []
for i in range(1, 6):
    chart.append({'Label': i, 'Color': color_map[i]})
chart_element = ChartModule(chart)

hex_model_params = model_params.copy()
hex_model_params['hex'] = True
hex_server = ModularServer(
    RockScissorsPaperEmpty, [hex_canvas_element, chart_element], "Rock Scissors Paper", hex_model_params
)

square_model_params = model_params.copy()
square_model_params['hex'] = False
square_server = ModularServer(
    RockScissorsPaperEmpty, [square_canvas_element, chart_element], "Rock Scissors Paper", square_model_params
)