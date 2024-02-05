import mesa
import numpy as np
import seaborn as sns
from .cell import Cell
from mesa.datacollection import DataCollector

class RockScissorsPaper(mesa.Model):
    """
    Represents the 2-dimensional array of cells in Rock-Scissors-Paper Game.
    """

    def __init__(self, rules, n_species, threshold, color_map=sns.color_palette().as_hex(), width=50, height=50):
        """
        Create a new playing area of (width, height) cells.
        """
        super().__init__()

        self.rules = rules
        self.threshold = threshold
        self.n_species = n_species
        self.color_map = color_map

        # Set up the grid and schedule.

        # Use SimultaneousActivation which simulates all the cells
        # computing their next state simultaneously.  This needs to
        # be done because each cell's next state depends on the current
        # state of all its neighbors -- before they've changed.
        self.schedule = mesa.time.SimultaneousActivation(self)

        # Use a simple grid, where edges wrap around.
        self.grid = mesa.space.SingleGrid(width, height, torus=True)

        # Place a cell at each location, initializing it as ROCK, SCISSOR, or PAPER
        for _, (x, y) in self.grid.coord_iter():
            cell_init_state = self.random.choice(range(0, self.n_species))
            cell = Cell(pos=(x, y), model=self, init_state=cell_init_state)
            self.grid.place_agent(cell, (x, y))
            self.schedule.add(cell)

        self.running = True
        
        model_reporter = {}
        for i in range(self.n_species):
            model_reporter[i] = lambda model, species=i: model.count_cells(species)
        self.datacollector = DataCollector(
            model_reporter
        )
        self.datacollector.collect(self)

    def count_cells(self, species):
        """
        Helper method to count the number of cells in the given state.
        """
        return sum([1 for cell in self.schedule.agents if cell.state == species])

    def step(self):
        """
        Have the scheduler advance each cell by one step
        """
        self.schedule.step()
        self.datacollector.collect(self)