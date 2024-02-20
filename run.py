from rock_scissors_paper.server import square_server, hex_server
from rock_scissors_paper.server_SSR import square_empty_server, hex_empty_server, model_params
# from mesa.visualization import CanvasHexGrid, CanvasGrid
# from .portrayal import portraySquarePatch, portrayHexPatch
# from .model_empty import RockScissorsPaperEmpty
# from .model import RockScissorsPaper
import mesa
model_params = {}
model_params["replay"] = mesa.visualization.Checkbox("Replay cached run?", False)

while True:
    grid_type = input("Enter 'S' for square or 'H' for hexagonal cells: ")
    if grid_type in ["S", "H"]:
        break
    else:
        print("Invalid input")

while True:
    model_type = input("Enter '1' for square; '2' for swap-fight-reproduce model: ")
    if model_type in ["1", "2"]:
        break
    else:
        print("Invalid input")

# while True:
#     width = input("Enter the width of the grid (in [1, 200]): ")
#     if width.isdigit() and 1 <= int(width) <= 200:
#         width = int(width)
#         break
#     else:
#         print("Invalid input")

# while True:
#     height = input("Enter the height of the grid (in [1, 200]): ")
#     if height.isdigit() and 1 <= int(height) <= 200:
#         height = int(height)
#         break
#     else:
#         print("Invalid input")

if grid_type == "S":
    server = square_server if model_type == "1" else square_empty_server
else:
    server = hex_server if model_type == "1" else hex_empty_server

server.launch(open_browser=True)