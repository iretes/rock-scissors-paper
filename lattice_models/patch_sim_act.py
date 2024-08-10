import mesa
import numpy as np

class PatchSimAct(mesa.Agent):
    """Represents a single patch in the simulation."""

    def __init__(self, pos, model, init_state):
        """
        Create a patch, in the given state, at the given x, y position.
        """
        super().__init__(pos, model)
        self.rules = model.rules
        self.n_species = model.n_species
        self.color_map = model.color_map
        self.threshold = model.threshold
        self.x, self.y = pos
        self.state = init_state
        self._nextState = None

    def step(self):
        """
        Compute the next state of the path according to the rules of the game and
        the number of defeats of each type.
        The state is not changed here, but is just computed and stored in self._nextState,
        because our current state may still be necessary for our neighbors
        to calculate their next state.
        """

        # assume nextState is unchanged, unless changed below
        self._nextState = self.state

        # get the neighbors
        neighbors = self.model.grid.get_neighbors((self.x, self.y), moore=True)

        # count the number of defeats of each type
        defeat_counts = np.zeros(self.n_species)
        for neighbor in neighbors:
            if neighbor.state != self.state and self.state in self.rules[neighbor.state]:
                defeat_counts[neighbor.state] += 1
        
        # compute the winning species
        winners = np.argwhere(defeat_counts == np.max(defeat_counts)).reshape(-1)
        self.random.shuffle(winners)
        for i in range(len(winners)):
            if defeat_counts[winners[i]] >= self.threshold:
                self._nextState = winners[i]
                break

    def advance(self):
        """
        Set the state to the new state, computed in the method step().
        """
        self.state = self._nextState
