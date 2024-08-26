import mesa
import numpy as np
from .patch_mobility import PatchMobility
from mesa.datacollection import DataCollector

class RSPMobility(mesa.Model):
    """
    This model is based on the Rock-Paper-Scissors model implemented in NetLogo.

    References:
    [1] Reichenbach, Tobias, Mauro Mobilia, and Erwin Frey.
    "Mobility promotes and jeopardizes biodiversity in rock-paper-scissors games."
    Nature 448.7157 (2007): 1046-1049.
    [2] Head, B., Grider, R. and Wilensky, U. (2017). NetLogo Rock Paper Scissors model.
    http://ccl.northwestern.edu/netlogo/models/RockPaperScissors.
    Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.
    """

    # key: species, value: list of species that the key species can beat
    # e.g. ROCK (0) beats SCISSOR (1), SCISSOR (1) beats PAPER (2), PAPER (2) beats ROCK (0)
    rules3 = {1: [2], 2: [3], 3: [1]}
    rules4 = {1: [2], 2: [3], 3: [4], 4: [1]}
    rules5 = {1: [2,3], 2: [3,4], 3: [4,5], 4: [5,1], 5: [1,2]}

    def __init__(
            self,
            init0, init1, init2, init3, init4, init5,
            swap_exp, reproduce_exp, select_exp,
            n_species, color_map, width=50, height=50
        ):
        """
        Initialize the model with the given parameters.
        """
        super().__init__()

        self.n_species = n_species

        event_repetitions = (width * height) // 3
        self.expected_swap = (10**swap_exp)*event_repetitions
        self.expected_reproduce = (10**reproduce_exp)*event_repetitions
        self.expected_select = (10**select_exp)*event_repetitions

        self.color_map = color_map

        if self.n_species == 3:
            self.probabilities = [init0, init1, init2, init3]
            self.rules = self.rules3
        elif self.n_species == 4:
            self.probabilities = [init0, init1, init2, init3, init4]
            self.rules = self.rules4
        else: # n_species == 5
            self.probabilities = [init0, init1, init2, init3, init4, init5]
            self.rules = self.rules5

        # Set up the grid and schedule.

        self.schedule = mesa.time.RandomActivation(self)

        # Use a simple grid, where edges wrap around.
        self.grid = mesa.space.SingleGrid(width, height, torus=True)

        # Place a patch at each location, initializing it as ROCK, SCISSOR, or PAPER
        for _, (x, y) in self.grid.coord_iter():
            patch_init_state = self.random.choices(range(0, self.n_species+1), weights=self.probabilities, k=1)[0]
            patch = PatchMobility(pos=(x, y), model=self, init_state=patch_init_state)
            self.grid.place_agent(patch, (x, y))
            self.schedule.add(patch)

        self.running = True
        
        model_reporter = {}
        for i in range(self.n_species+1):
            model_reporter[i] = lambda model, species=i: model.count_patches(species)
        
        self.datacollector = DataCollector(
            model_reporter
        )
        self.datacollector.collect(self)

    def count_patches(self, species):
        """
        Helper method to count the number of patches in the given state.
        """
        return sum([1 for patch in self.schedule.agents if patch.state == species])

    def step(self):
        """
        Compute the number of global events and have the scheduler advance each
        patch by one step.
        """

        # create a list of events with random Poisson distribution
        self.events = []
        self.events.extend(['swap'] * int(np.random.poisson(self.expected_swap)))
        self.events.extend(['reproduce'] * int(np.random.poisson(self.expected_reproduce)))
        self.events.extend(['select'] * int(np.random.poisson(self.expected_select)))
        
        # shuffle events
        self.random.shuffle(self.events)

        self.schedule.step()
        self.datacollector.collect(self)

        n_existint_species = sum([1 for i in range(1, self.n_species+1) if self.count_patches(i) == 0])
        if n_existint_species == self.n_species-1:
            self.running = False