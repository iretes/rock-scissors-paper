import mesa
from .model import RockScissorsPaper
from .portrayal import portrayCell
from mesa.visualization.modules import ChartModule
from mesa.visualization import StaticText

# prendi argomenti da linea di comando...

# Make a world that is 50x50, on a 500x500 display.
canvas_element = mesa.visualization.CanvasGrid(portrayCell, 100, 100, 500, 500)

rules_3_species = {
    (0, 1): 0,
    (1, 2): 1,
    (2, 0): 2
}
rules_3_species = {
    (0, 1): 0,
    (1, 2): 1,
    (2, 0): 2
}

rules_4_species_asym = {
    (0, 1): 0,
    (0, 2): 0,
    (1, 2): 1,
    (1, 3): 1,
    (2, 3): 2,
    (3, 0): 3
}

rules_4_species_sym = {
    (0, 1): 0,
    (0, 2): 0,
    (1, 2): 1,
    (1, 3): 1,
    (2, 3): 2,
    (2, 0): 2,
    (3, 0): 3,
    (3, 1): 3
}

rules_5_species = {
    (0, 1): 0,
    (0, 2): 0,
    (1, 2): 1,
    (1, 3): 1,
    (2, 3): 2,
    (2, 4): 2,
    (3, 0): 3,
    (3, 4): 3,
    (4, 0): 4,
    (4, 1): 4
}

for contestanst, winner in rules_4_species_sym.items():
    if winner == contestanst[0]:
        print(contestanst[0]>contestanst[1])
    else:
        print(contestanst[1]>contestanst[0])

N_SPECIES = 4
color_map = {
    0: 'red',
    1: 'yellow',
    2: 'purple',
    3: 'green',
    4: 'blue'
}

str = '<b>RULES</b><br />'
for contestanst, winner in rules_4_species_sym.items():
    if winner == contestanst[0]:
        str += f'{contestanst[0]} > {contestanst[1]}<br />'
    else:
        str += f'{contestanst[1]} > {contestanst[0]}<br />'
model_params = {
    "height": 100,
    "width": 100,
    "rules": rules_4_species_sym,#rules_5_species,#rules_4_species_asym,
    "rules_descr": StaticText(str),
    "n_species": N_SPECIES,
    "color_map": color_map
}

chart = []
for i in range(N_SPECIES):
    chart.append({'Label': i, 'Color': color_map[i]})
chart_element = mesa.visualization.ChartModule(chart)

server = mesa.visualization.ModularServer(
    RockScissorsPaper, [canvas_element, chart_element], "Rock Scissors Paper", model_params
)