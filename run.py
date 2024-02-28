import mesa
from rock_scissors_paper.model_SSR import RockScissorsPaperSSR
from rock_scissors_paper.model_MV import RockScissorsPaperMV
from rock_scissors_paper.portrayal import portraySquarePatch, portrayHexPatch
from rock_scissors_paper.server_SSR import model_params_SSR, chart_element_SSR
from rock_scissors_paper.server_MV import model_params_MV, chart_element_MV
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
while True:
    model_type = input("Enter '1' for majority-voting model; '2' for swap-fight-reproduce model: ")
    if model_type in ["1", "2"]:
        break
    else:
        print("Invalid input")

if grid_type == "S":
    canvas_element = CanvasGrid(
        portraySquarePatch,
        grid_width=grid_width,
        grid_height=grid_height,
        canvas_width=400,
        canvas_height=400
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

model_params = model_params_MV if model_type == MAJORITY_VOTING else model_params_SSR
model_params['height'] = grid_height
model_params['width'] = grid_width
model_params['rules_descr'] = StaticText(rules_descr)
model_params['hex'] = True if grid_type == "H" else False
model = RockScissorsPaperMV if model_type == MAJORITY_VOTING else RockScissorsPaperSSR
chart_element = chart_element_MV if model_type == MAJORITY_VOTING else chart_element_SSR
model_descr = "Rock Scissors Paper: Majority Voting" if model_type == MAJORITY_VOTING else "Rock Scissors Paper: Swap Fight Reproduce"

server = ModularServer(
    model, [canvas_element, chart_element], model_descr, model_params
)
server.launch(open_browser=True)