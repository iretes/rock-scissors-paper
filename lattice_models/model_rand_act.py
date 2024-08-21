import mesa
from .patch_rand_act import PatchRandAct
from mesa.datacollection import DataCollector

class RSPRandAct(mesa.Model):
    """
    This model is based on the Rock-Paper-Scissors model proposed by Frean and Abraham.

    Reference:
    Frean, Marcus, and Edward R. Abraham. "Rock-scissors-paper and the survival of the weakest." 
    Proceedings of the Royal Society of London. Series B: Biological Sciences 268.1474 (2001): 1323-1327.
    """

    # key: species, value: list of species that the key species can beat
    # e.g. ROCK (0) beats SCISSOR (1), SCISSOR (1) beats PAPER (2), PAPER (2) beats ROCK (0)
    rules3 = {0: [1], 1: [2], 2: [0]}
    rules4 = {0: [1], 1: [2], 2: [3], 3: [0]}
    rules5 = {0: [1,2], 1: [2,3], 2: [3,4], 3: [4,0], 4: [0,1]}

    def __init__(self,
                 init0, init1, init2, init3, init4,
                 invrate0, invrate1, invrate2, invrate3, invrate4,
                 n_species,
                 color_map,
                 increase_rate=False,
                 width=50, height=50):
        """
        Create a new playing area of (width, height) patches.
        """
        super().__init__()

        self.n_species = n_species
        self.color_map = color_map
        self.increase_rate = increase_rate
        if self.n_species == 3:
            self.init_probabilities = [init0, init1, init2]
            self.invasion_rates = [invrate0, invrate1, invrate2]
            self.rules = self.rules3
        elif self.n_species == 4:
            self.init_probabilities = [init0, init1, init2, init3]
            self.invasion_rates = [invrate0, invrate1, invrate2, invrate3]
            self.rules = self.rules4
        else: # n_species == 5
            self.init_probabilities = [init0, init1, init2, init3, init4]
            self.invasion_rates = [invrate0, invrate1, invrate2, invrate3, invrate4]
            self.rules = self.rules5

        # set up agent scheduler
        self.schedule = mesa.time.RandomActivation(self)

        # use a simple grid, where edges wrap around.
        self.grid = mesa.space.SingleGrid(width, height, torus=True)

        # place a patch at each location, randomly initializing it according to the given initial proportions
        for _, (x, y) in self.grid.coord_iter():
            patch_init_state = self.random.choices(range(self.n_species), weights=self.init_probabilities, k=1)[0]
            patch = PatchRandAct(pos=(x, y), model=self, init_state=patch_init_state)
            self.grid.place_agent(patch, (x, y))
            self.schedule.add(patch)

        self.running = True
        
        # collect data
        model_reporter = {}
        for i in range(self.n_species):
            model_reporter[i] = lambda model, species=i: model.count_patches(species)
        if self.increase_rate:
           model_reporter['increased_rate'] = lambda model: model.invasion_rates[0] # TODO: lambda model: model.compute_average_invrate0()=
        self.datacollector = DataCollector(
            model_reporter
        )
        self.datacollector.collect(self)

    def count_patches(self, species):
        """
        Helper method to count the number of patches in the given state.
        """
        return sum([1 for patch in self.schedule.agents if patch.state == species])
    
    def compute_average_invrate0(self): # TODO: delete?
        rates = [patch.invasion_rate for patch in self.schedule.agents if patch.state == 0]
        return sum(rates) / len(rates)

    def step(self):
        """
        Have the scheduler advance each patch by one step.
        """
        self.schedule.step()
        self.datacollector.collect(self)

        n_existint_species = sum([1 for i in range(self.n_species) if self.count_patches(i) == 0])
        if n_existint_species == self.n_species-1:
            self.running = False