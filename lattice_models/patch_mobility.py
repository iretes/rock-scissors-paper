import mesa

class PatchMobility(mesa.Agent):
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
        Compute the next state of the patch and/or of a randomly chosen
        neighbor, according to the event that is going to happen.
        """
        # Get the neighbors
        neighbors = self.model.grid.get_neighbors((self.x, self.y), moore=False) # 4 neighbors

        # get the action
        if len(self.model.events) == 0:
            return
        action = self.model.events.pop(0)

        # select a random neighbor
        neighbor = self.random.choice(neighbors)

        # act
        if action == 'swap':
            self._nextState = neighbor.state
            neighbor.state = self.state
            self.state = self._nextState
        elif action == 'select':
            if neighbor.state != 0 and self.state in self.rules[neighbor.state]:
                self.state = 0
            if self.state != 0 and neighbor.state in self.rules[self.state]:
                neighbor.state = 0
        else:
            if neighbor.state == 0:
                neighbor.state = self.state
            elif self.state == 0:
                self.state = neighbor.state
