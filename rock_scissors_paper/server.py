import mesa
from .model import RockScissorsPaper
from .portrayal import portrayCell
from mesa.visualization.modules import ChartModule
from mesa.visualization import StaticText, Choice

# Make a world that is 50x50, on a 500x500 display.
canvas_element = mesa.visualization.CanvasGrid(portrayCell, 100, 100, 500, 500)

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
    "height": 100,
    "width": 100,
    "rules_descr": StaticText(rules_descr),
    "n_species": Choice(
        "Number of species",
        value=3,
        choices=[3,4,5],
        description="Number of species"
    ),
    "prob0": mesa.visualization.Slider(
        "Fraction of individuals of species 0",
        0.33,
        0,
        1,
        0.05,
        description="Fraction of individuals of species 0",
    ),
    "prob1": mesa.visualization.Slider(
        "Fraction of individuals of species 1",
        0.33,
        0,
        1,
        0.05,
        description="Fraction of individuals of species 1",
    ),
    "prob2": mesa.visualization.Slider(
        "Fraction of individuals of species 2",
        0.33,
        0,
        1,
        0.05,
        description="Fraction of individuals of species 2",
    ),
    "prob3": mesa.visualization.Slider(
        "Fraction of individuals of species 3",
        0,
        0,
        1,
        0.05,
        description="Fraction of individuals of species 3",
    ),
    "prob4": mesa.visualization.Slider(
        "Fraction of individuals of species 4",
        0,
        0,
        1,
        0.05,
        description="Fraction of individuals of species 4",
    ),
    "color_map": color_map
}

# TODO: capisci meglio pesi random (0.33?), capisci se c'è modo sequenziale...
# TODO: commenti
# TODO: sviluppa come agenti

chart = []
for i in range(5):
    chart.append({'Label': i, 'Color': color_map[i]})
chart_element = mesa.visualization.ChartModule(chart)

server = mesa.visualization.ModularServer(
    RockScissorsPaper, [canvas_element, chart_element], "Rock Scissors Paper", model_params
)