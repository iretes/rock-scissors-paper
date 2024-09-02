# Rock-Scissors-Paper: The Game That Sustains Biodiversity and Regulates Biological Clocks

This project reproduces the experiments conducted by Frean et al. [[1]](#references) and Reichenbach et al. [[2], [3]](#references) to study a system involving three species in a competitive loop: a rock beats (and replicates into) a pair of scissors, scissors beat a sheet of paper and paper beats a rock. The self-referential nature of the competitive loop leads to counterintuitive phenomena, such as the expectation that the least competitive species will have the largest population, ultimately preserving diversity. The proposed model is examined through various formalisms, and its properties are analyzed within each framework.

Additionally, an oscillatory network of transcriptional regulators known as the Repressilator is explored. This network consists of a feedback loop involving three genes, each encoding a protein that represses the expression of the next gene in the loop. The dynamic behavior of the Repressilator mirrors the competitive interactions of the rock-scissors-paper game, as each component cyclically inhibits the next. The analysis centers on how this cyclical repression generates oscillatory patterns, enabling the implementation of a biological clock in *Escherichia Coli*, as detailed in [[4]](#references).

## Ecological models

### Long range dispersal model

The notebook [`long_range_simulations.ipynb`](./notebooks/long_range_simulations.ipynb) analyzes simulations of the long-range dispersal model, where individuals are modeled as gas molecules, and interactions occur between any pair.

The model is examined under both discrete and continuous time frameworks. For the continuous time approach, the differential equation system defining the model is solved using the [`scipy.integrate`](https://docs.scipy.org/doc/scipy/reference/integrate.html#module-scipy.integrate) package. Additionally, the model is reframed in terms of chemical reactions for stochastic simulations, which are conducted using the [`StochPy`](https://stochpy.sourceforge.net) package. It is further examined as a continuous-time Markov chain with the [`PRISM`](https://www.prismmodelchecker.org) stochastic model checker and as a Petri net with the tool [`Charlie`](https://www-dssz.informatik.tu-cottbus.de/DSSZ/Software/Charlie).

### Lattice model

The notebook [`lattice_simulations.ipynb`](./notebooks/lattice_simulations.ipynb) analyzes simulations of the local dispersal model, where individuals are situated on a lattice and interact solely with their neighbors.

This lattice-based model was developed using the [`Mesa`](https://mesa.readthedocs.io/en/stable/) framework.

#### How to run simulations from your browser

First, install the dependencies executing the following command:

```bash
pip install -r requirements.txt
```

To interactively run the model, execute the following command:

```bash
python ./run_lattice_model.py
```

Set the grid's width and height, choose the model to run (either the one based on [[1]](#references), [[2]](#references), or a variant where agents activate simultaneously; see [here](./notebooks/lattice_simulations.ipynb) for more details), and then open your browser to http://127.0.0.1:8521/.

The sliders labeled 'Initial weight of species *' allow you to set the weights used by the [`random.choices`](https://docs.python.org/3/library/random.html#random.choices) method (from the Python Standard Library) for initializing grid patches with individuals. These weights don't need to sum to $1$.

The sliders 'Swap rate', 'Reproduce rate' and 'Select rate' in the model based on [[2]](#references) have the same meaning as those in the NetLogo Rock-Paper-Scissors model [[3]](#references).

#### Demo

https://github.com/iretes/rock-scissors-paper/assets/46034276/2a1055cc-fee6-4a60-b513-3b3d7210b7ad

## Repressilator model

The notebook [`repressilator.ipynb`](./notebooks/repressilator.ipynb) analyzes simulations of the Repressilator model.

The dynamics of this system are simulated by solving the differential equations governing protein concentration changes, using the [`scipy.integrate`](https://docs.scipy.org/doc/scipy/reference/integrate.html#module-scipy.integrate) package.

## Directory structure

The project's directory structure includes the following main folders and files:
```
rock-scissors-paper
  │── lattice_models        # folder storing Mesa implementations of lattice models
  │── long_range_models     # folder storing long-range dispersal models in different formalisms
  │── notebooks             # folder storing Jupyter notebooks analyzing the models
  │── results               # folder storing simulation results
  │── requirements.txt      # requirements file for pip
  └── run_lattice_model.py  # script to run lattice models web interface
```

## References
- [1] Frean, Marcus, and Edward R. Abraham. "Rock–scissors–paper and the survival of the weakest." Proceedings of the Royal Society of London. Series B: Biological Sciences 268.1474 (2001): 1323-1327.
- [2] Reichenbach, Tobias, Mauro Mobilia, and Erwin Frey. "Mobility promotes and jeopardizes biodiversity in rock–paper–scissors games." Nature 448.7157 (2007): 1046-1049.
- [3] Head, B., Grider, R. and Wilensky, U. (2017). [NetLogo Rock Paper Scissors model](http://ccl.northwestern.edu/netlogo/models/RockPaperScissors). Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.
- [4] Elowitz M., Bois J. and Marken J. (2022). ["Biological Circuits Design"](https://biocircuits.github.io/chapters/09_repressilator.html). California Institute of Technology.

---
This project was developed for the “Computational Models for Complex Systems” course at the University of Pisa (a.y. 2023/2024).