from rock_scissors_paper.server import square_server, hex_server

while True:
    grid_type = input("Enter 'S' for square or 'H' for hexagonal cells: ")
    if grid_type in ["S", "H"]:
        break
    else:
        print("Invalid input")

if grid_type == "S":
    server = square_server
else:
    server = hex_server

server.launch(open_browser=True)