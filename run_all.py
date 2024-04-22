import mesa
from rock_scissors_paper.model_SSR import RockScissorsPaperSSR
from rock_scissors_paper.model_MV import RockScissorsPaperMV
from rock_scissors_paper.model_original import RockScissorsPaperO
from rock_scissors_paper.portrayal import portraySquarePatch, portrayHexPatch
from rock_scissors_paper.server_SSR import model_params_SSR, chart_element_SSR
from rock_scissors_paper.server_MV import model_params_MV, chart_element_MV
from rock_scissors_paper.server_original import model_params_O, chart_element_O
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

MAJORITY_VOTING = "1"
SWAP_FIGHT_REPRODUCE = "2"
ORIGINAL = "3"
while True:
    model_type = input("Enter '1' for majority-voting model; '2' for swap-fight-reproduce model; '3' for original implementation: ")
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

model_params = model_params_MV if model_type == MAJORITY_VOTING else model_params_SSR if model_type == SWAP_FIGHT_REPRODUCE else model_params_O
model_params['height'] = grid_height
model_params['width'] = grid_width
model_params['rules_descr'] = StaticText(rules_descr)
model_params['hex'] = True if grid_type == "H" else False
model = RockScissorsPaperMV if model_type == MAJORITY_VOTING else RockScissorsPaperSSR if model_type == SWAP_FIGHT_REPRODUCE else RockScissorsPaperO
chart_element = chart_element_MV if model_type == MAJORITY_VOTING else chart_element_SSR if model_type == SWAP_FIGHT_REPRODUCE else chart_element_O
model_descr = "Rock Scissors Paper: Majority Voting" if model_type == MAJORITY_VOTING else "Rock Scissors Paper: Swap Fight Reproduce" if model_type == SWAP_FIGHT_REPRODUCE else "Rock Scissors Paper: Original"

server = ModularServer(
    model, [canvas_element, chart_element], model_descr, model_params
)
server.launch(open_browser=True)