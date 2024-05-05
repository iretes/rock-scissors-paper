import mesa
from .patch_random_act import Patch
from mesa.datacollection import DataCollector

class RockScissorsPaper(mesa.Model):
    """
    A system with three species in a competitive loop: a rock beats a pair of scissors,
    scissors beat a sheet of paper and paper beats a rock.
    """

    rules = {0: [1], 1: [2], 2: [0]}

    def __init__(self, hex,
                 r0, s0, p0,
                 Pr, Ps, Pp,
                 color_map, 
                 increase_rate=False,
                 width=50, height=50):
        """
        Create a new playing area of (width, height) patches.
        """
        super().__init__()

        self.hex = hex

        self.n_species = 3

        self.color_map = color_map

        self.increase_rate = increase_rate
        
        self.probabilities = [r0, s0, p0]
        self.invasion_rates = [Pr, Ps, Pp]
        self.rules = self.rules

        # Set up the grid and schedule.

        self.schedule = mesa.time.RandomActivation(self)

        # Use a simple grid, where edges wrap around.
        if hex:
            self.grid = mesa.space.HexSingleGrid(width, height, torus=True)
        else:
            self.grid = mesa.space.SingleGrid(width, height, torus=True)

        # Place a patch at each location, initializing it as ROCK, SCISSOR, or PAPER
        for _, (x, y) in self.grid.coord_iter():
            patch_init_state = self.random.choices(range(self.n_species), weights=self.probabilities, k=1)[0]
            patch = Patch(pos=(x, y), model=self, init_state=patch_init_state)
            self.grid.place_agent(patch, (x, y))
            self.schedule.add(patch)

        self.running = True
        
        model_reporter = {}
        for i in range(self.n_species):
            model_reporter[i] = lambda model, species=i: model.count_patches(species)
        if self.increase_rate:
            model_reporter['Pr'] = lambda model: model.invasion_rates[0]
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
        Have the scheduler advance each patch by one step
        """
        self.schedule.step()
        self.datacollector.collect(self)

        n_existint_species = sum([1 for i in range(self.n_species) if self.count_patches(i) == 0])
        if n_existint_species == self.n_species-1:
            self.running = False