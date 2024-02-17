import mesa
import numpy as np

class PatchEmpty(mesa.Agent):
    """Represents a single patch in the simulation."""

    def __init__(self, pos, model, init_state):
        """
        Create a patch, in the given state, at the given x, y position.
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
        Compute if the patch will be rock, scissors or paper at the next tick.  This is
        based on the number of rock, scissors and paper in the neighborhood.
        The state is not changed here, but is just computed and stored in self._nextState,
        because our current state may still be necessary for our neighbors
        to calculate their next state.
        """
        # Get the neighbors
        if self.model.hex:
            neighbors = self.model.grid.get_neighbors((self.x, self.y), include_center=False)
        else:
            neighbors = self.model.grid.get_neighbors((self.x, self.y), moore=True)

        # swap, fight, reproduce
        action = self.random.choice(['swap', 'fight', 'reproduce'])
        # select a random neighbor
        neighbor = self.random.choice(neighbors)
        # act
        if action == 'swap':
            self._nextState = neighbor.state
            neighbor.state = self.state
            self.state = self._nextState
        elif action == 'fight':
            if neighbor.state != 0 and self.state in self.rules[neighbor.state]:
                self.state = 0
            if self.state != 0 and neighbor.state in self.rules[self.state]:
                neighbor.state = 0
        else:
            if neighbor.state == 0:
                neighbor.state = self.state
            elif self.state == 0:
                self.state = neighbor.state
