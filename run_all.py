import mesa
from rock_scissors_paper.model_SSR import RockScissorsPaperSSR
from rock_scissors_paper.model_simultaneous_act import RockScissorsPaperSimultaneousActivation
from rock_scissors_paper.model_random_act import RockScissorsPaper
from rock_scissors_paper.portrayal import portraySquarePatch, portrayHexPatch
from rock_scissors_paper.server_SSR import model_params_SSR, chart_element_SSR
from rock_scissors_paper.server_simultaneous_act import model_params_simultaneous, chart_element_simultaneous
from rock_scissors_paper.server_random_act import model_params, chart_element
from mesa.visualization import CanvasHexGrid, CanvasGrid, StaticText, ModularServer

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

while True:
    grid_type = input("Enter 'S' for square or 'H' for hexagonal cells: ")
    if grid_type in ["S", "H"]:
        break
    else:
        print("Invalid input")

SIMULTANEOUS_ACTIVATIONS = "1"
SWAP_FIGHT_REPRODUCE = "2"
RANDOM_ACTIVATIONS = "3"
while True:
    model_type = input("Enter '1' for simultaneous activations; '2' for swap-fight-reproduce model; '3' for random activations: ")
    if model_type in ["1", "2", "3"]:
        break
    else:
        print("Invalid input")

if grid_type == "S":
    canvas_element = CanvasGrid(
        portraySquarePatch,
        grid_width=grid_width,
        grid_height=grid_height,
        canvas_width=600,
        canvas_height=600
        )
else:
    canvas_element = CanvasHexGrid(
        portrayHexPatch,
        grid_width=grid_width,
        grid_height=grid_height,
        canvas_width=450,
        canvas_height=450
    )

rules_descr = '<b>Rules with 3 species:</b><br />'
for key, val in RockScissorsPaperSSR.rules3.items():
    rules_descr += f'{key} > {val[0]}<br />'
rules_descr += '<b>Rules with 4 species:</b><br />'
for key, val in RockScissorsPaperSSR.rules4.items():
    rules_descr += f'{key} > {val[0]}<br />'
rules_descr += '(<0,2> and <1,3> do not compete)<br />'
rules_descr += '<b>Rules with 5 species:</b><br />'
for key, val in RockScissorsPaperSSR.rules5.items():
    rules_descr += f'{key} > {val[0]}, {val[1]}<br />'

model_params = model_params_simultaneous if model_type == SIMULTANEOUS_ACTIVATIONS else model_params_SSR if model_type == SWAP_FIGHT_REPRODUCE else model_params
model_params['height'] = grid_height
model_params['width'] = grid_width
model_params['rules_descr'] = StaticText(rules_descr)
model_params['hex_grid'] = True if grid_type == "H" else False
model = RockScissorsPaperSimultaneousActivation if model_type == SIMULTANEOUS_ACTIVATIONS else RockScissorsPaperSSR if model_type == SWAP_FIGHT_REPRODUCE else RockScissorsPaper
chart_element = chart_element_simultaneous if model_type == SIMULTANEOUS_ACTIVATIONS else chart_element_SSR if model_type == SWAP_FIGHT_REPRODUCE else chart_element
model_descr = "Rock Scissors Paper: Simultaneous Activations" if model_type == SIMULTANEOUS_ACTIVATIONS else "Rock Scissors Paper: Swap Fight Reproduce" if model_type == SWAP_FIGHT_REPRODUCE else "Rock Scissors Paper: Random activations"

server = ModularServer(
    model, [canvas_element, chart_element], model_descr, model_params
)
server.launch(open_browser=True)