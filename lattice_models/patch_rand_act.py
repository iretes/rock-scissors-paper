import mesa

class PatchRandAct(mesa.Agent):
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
        Compute the next state of the patch according to the rules of the game
        and the invasion rates of the species.
        """
        # get the neighbors
        neighbors = self.model.grid.get_neighbors((self.x, self.y), moore=True)

        # select a random neighbor
        neighbor = self.random.choice(neighbors)
        
        # if the neighbor can be defeated
        if neighbor.state in self.rules[self.state]:
            # change the neighbor state according to the invasion rate
            win_rate = self.model.invasion_rates[self.state]
            new_neigh_state = self.random.choices(
                [self.state, neighbor.state],
                weights=[win_rate, 1-win_rate],
                k=1)[0]
            neighbor.state = new_neigh_state
            
            # increase species 0 invasion rate if needed
            if (self.model.increase_rate and self.state==0 and \
                new_neigh_state==self.state and self.model.schedule.steps>100):
                rand = self.random.uniform(0, 1e-4)
                new_rate = self.model.invasion_rates[self.state] + rand
                if 0 < new_rate < 1:
                    self.model.invasion_rates[self.state] = new_rate