import mesa

class PatchO(mesa.Agent):
    """Represents a single patch in the simulation."""

    def __init__(self, pos, model, init_state):
        """
        Create a patch, in the given state, at the given x, y position.
        """
        super().__init__(pos, model)
        self.rules = model.rules
        self.invasion_rates = model.invasion_rates
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

        # select a random neighbor
        neighbor = self.random.choice(neighbors)

        # TODO: doppia azione?
        # if self.state in self.rules[neighbor.state]:
        #     defeat_rate = self.invasion_rates[neighbor.state]
        #     self.state = self.random.choices(
        #         [neighbor.state, self.state],
        #         weights=[defeat_rate, 1-defeat_rate],
        #         k=1)[0]
        # elif neighbor.state in self.rules[self.state]:
        #     win_rate = self.invasion_rates[self.state]
        #     neighbor.state = self.random.choices(
        #         [self.state, neighbor.state],
        #         weights=[win_rate, 1-win_rate],
        #         k=1)[0]
            
        if neighbor.state in self.rules[self.state]:
            win_rate = self.invasion_rates[self.state]
            neighbor.state = self.random.choices(
                [self.state, neighbor.state],
                weights=[win_rate, 1-win_rate],
                k=1)[0]