import mesa
import numpy as np
from enum import Enum

class Cell(mesa.Agent):
    """Represents a single cell in the simulation."""

    def __init__(self, pos, model, init_state):
        """
        Create a cell, in the given state, at the given x, y position.
        """
        super().__init__(pos, model)
        self.rules = model.rules
        self.n_species = model.n_species
        self.color_map = model.color_map
        self.x, self.y = pos
        self.state = init_state
        self._nextState = None

    def step(self):
        """
        Compute if the cell will be rock, scissors or paper at the next tick.  This is
        based on the number of rock, scissors and paper in the neighborhood.
        The state is not changed here, but is just computed and stored in self._nextState,
        because our current state may still be necessary for our neighbors
        to calculate their next state.
        """

        # Assume nextState is unchanged, unless changed below.
        self._nextState = self.state
        # Get the neighbors (Moore neighborhood, including diagonals)
        neighbors = self.model.grid.get_neighbors((self.x, self.y), True)
        # Count the number defeats of each type
        defeat_counts = np.zeros(self.n_species)
        for neighbor in neighbors:
            if neighbor.state == self.state:
                continue
            if (neighbor.state, self.state) in self.rules:
                contestants = (neighbor.state, self.state)
            else:
                contestants = (self.state, neighbor.state)
            winner = self.rules[contestants]
            defeat_counts[winner] += 1
        # Compute the winner species
        winners = np.argwhere(defeat_counts == np.max(defeat_counts)).reshape(-1)
        np.random.shuffle(winners)
        for i in range(len(winners)):
            if defeat_counts[winners[i]] >= 3: # TODO: dipende dal vicinato
                self._nextState = winners[i]
                break

    def advance(self):
        """
        Set the state to the new computed state -- computed in step().
        """
        self.state = self._nextState
