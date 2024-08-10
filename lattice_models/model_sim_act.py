import mesa
from .patch_sim_act import PatchSimAct
from mesa.datacollection import DataCollector

class RSPSimAct(mesa.Model):
    """
    A system with three species in a competitive loop: a rock beats a pair of scissors,
    scissors beat a sheet of paper and paper beats a rock.
    """

    rules3 = {0: [1], 1: [2], 2: [0]}
    rules4 = {0: [1], 1: [2], 2: [3], 3: [0]}
    rules5 = {0: [1,2], 1: [2,3], 2: [3,4], 3: [4,0], 4: [0,1]}

    def __init__(self, init0, init1, init2, init3, init4, n_species, color_map, width=50, height=50):
        """
        Create a new playing area of (width, height) patches.
        """
        super().__init__()

        self.n_species = n_species
        self.color_map = color_map

        if self.n_species == 3:
            self.probabilities = [init0, init1, init2]
            self.threshold = 3
            self.rules = self.rules3
        elif self.n_species == 4:
            self.probabilities = [init0, init1, init2, init3]
            self.threshold = 2
            self.rules = self.rules4
        else: # n_species == 5
            self.probabilities = [init0, init1, init2, init3, init4]
            self.threshold = 3
            self.rules = self.rules5

        # set up agent scheduler
        self.schedule = mesa.time.SimultaneousActivation(self)

        # use a simple grid, where edges wrap around.
        self.grid = mesa.space.SingleGrid(width, height, torus=True)

        # place a patch at each location, initializing it as ROCK, SCISSOR, or PAPER
        for _, (x, y) in self.grid.coord_iter():
            patch_init_state = self.random.choices(range(self.n_species), weights=self.probabilities, k=1)[0]
            patch = PatchSimAct(pos=(x, y), model=self, init_state=patch_init_state)
            self.grid.place_agent(patch, (x, y))
            self.schedule.add(patch)

        self.running = True
        
        # collect data
        model_reporter = {}
        for i in range(self.n_species):
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
        Have the scheduler advance each patch by one step.
        """
        self.schedule.step()
        self.datacollector.collect(self)

        n_existint_species = sum([1 for i in range(self.n_species) if self.count_patches(i) == 0])
        if n_existint_species == self.n_species-1:
            self.running = False