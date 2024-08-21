import mesa
from lattice_models.model_mobility import RSPMobility
from lattice_models.model_sim_act import RSPSimAct
from lattice_models.model_rand_act import RSPRandAct
from lattice_models.portrayal import portraySquarePatch
from lattice_models.server_mobility import model_params_mobility, chart_element_mobility
from lattice_models.server_sim_act import model_params_simact, chart_element_simact
from lattice_models.server_rand_act import model_params_randact, chart_element_randact
from mesa.visualization import CanvasGrid, StaticText, ModularServer

while True:
    grid_width = input("Enter the width of the grid (in [1, 200]): ")
    if grid_width.isdigit() and 1 <= int(grid_width) <= 200:
        grid_width = int(grid_width)
        break
    else:
        print("Invalid input")

while True:
    grid_height = input("Enter the height of the grid (in [1, 200]): ")
    if grid_height.isdigit() and 1 <= int(grid_height) <= 200:
        grid_height = int(grid_height)
        break
    else:
        print("Invalid input")

RANDOM_ACTIVATIONS = "1"
SIMULTANEOUS_ACTIVATIONS = "2"
MOBILITY = "3"

while True:
    model_type = input(
        "Enter\n'1' for Frean and Abraham model with random activations of agents;"
        "\n'2' for the model using simultaneous activations of agents;"
        "\n'3' for Reichenbach, Mobilia and Frey model\n")
    if model_type in ["1", "2", "3"]:
        break
    else:
        print("Invalid input")

canvas_element = CanvasGrid(
    portraySquarePatch,
    grid_width=grid_width,
    grid_height=grid_height,
    canvas_width=600,
    canvas_height=600
    )

rules_descr = '<b>Rules with 3 species:</b><br />'
for key, val in RSPMobility.rules3.items():
    rules_descr += f'{key} > {val[0]}<br />'
rules_descr += '<b>Rules with 4 species:</b><br />'
for key, val in RSPMobility.rules4.items():
    rules_descr += f'{key} > {val[0]}<br />'
rules_descr += '(<2,4> and <1,3> do not compete)<br />'
rules_descr += '<b>Rules with 5 species:</b><br />'
for key, val in RSPMobility.rules5.items():
    rules_descr += f'{key} > {val[0]}, {val[1]}<br />'

if model_type == RANDOM_ACTIVATIONS:
    model_params = model_params_randact
    model = RSPRandAct
    chart_element = chart_element_randact
    model_descr = "Rock Scissors Paper: Frean and Abraham model with random activations of agents"
elif model_type == SIMULTANEOUS_ACTIVATIONS:
    model_params = model_params_simact
    model = RSPSimAct
    chart_element = chart_element_simact
    model_descr = "Rock Scissors Paper: model using simultaneous activations of agents"
else:
    model_params = model_params_mobility
    model = RSPMobility
    chart_element = chart_element_mobility
    model_descr = "Rock Scissors Paper: Reichenbach, Mobilia and Frey model"

model_params['height'] = grid_height
model_params['width'] = grid_width
model_params['rules_descr'] = StaticText(rules_descr)

server = ModularServer(
    model, [canvas_element, chart_element], model_descr, model_params
)
server.launch(open_browser=True)