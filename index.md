# Rock, Scissors, Paper: the survival of the weakest 🪨✂️📄

Analysis of a dynamical system with three species in a competitive loop: a rock beats (and replicates into) a pair of scissors, scissors beat a sheet of paper and paper beats a rock.

## Long range dispersal model

Click [here](./long_range_simulations.html) to view the notebook `long_range_simulations.ipynb`, which analyzes simulations of the long-range dispersal model. The model is examined under both discrete and continuous time frameworks. For the continuous time approach, the differential equation system defining the model is solved using the [`scipy.integrate`](https://docs.scipy.org/doc/scipy/reference/integrate.html#module-scipy.integrate) package. Additionally, the model is reframed in terms of chemical reactions for stochastic simulations, which are conducted using the [`StochPy`](https://stochpy.sourceforge.net) package. It is further examined as a continuous-time Markov chain with the [`PRISM`](https://www.prismmodelchecker.org) stochastic model checker.

## Lattice model

Click [here](./lattice_simulations.html) to view the notebook `lattice_simulations.ipynb`, which analyzes simulations of the local range dispersal model, where individuals are situated on a lattice and interact solely with their neighbors. This lattice-based model was developed using the [Mesa](https://mesa.readthedocs.io/en/stable/) framework.

### How to run simulations

After cloning the [GitHub repository](https://github.com/iretes/rock-scissors-paper), install the dependencies by executing the following command:

```bash
pip install -r requirements.txt
```

To interactively run the rock-scissors-paper model based on [1], where agents activating simultaneously, execute the following command:

```bash
python ./run_lattice_simact.py
```

To interactively run the rock-scissors-paper model where agents activating sequentially, execute the following command:

```bash
python ./run_lattice_randact.py
```

To interactively run the the rock-scissors-paper model based on [2], execute the following command:

```bash
python ./run_lattice_mobility.py
```

Then open your browser to http://127.0.0.1:8521/.

### Demo

<video width="640" height="480" controls loop="" muted="" autoplay="">
    <source src="https://github.com/iretes/rock-scissors-paper/assets/46034276/2a1055cc-fee6-4a60-b513-3b3d7210b7ad">
</video>

## References
- [1] Frean, Marcus, and Edward R. Abraham. "Rock–scissors–paper and the survival of the weakest." Proceedings of the Royal Society of London. Series B: Biological Sciences 268.1474 (2001): 1323-1327.
- [2] Reichenbach, Tobias, Mauro Mobilia, and Erwin Frey. "Mobility promotes and jeopardizes biodiversity in rock–paper–scissors games." Nature 448.7157 (2007): 1046-1049.

---
**Author**: Irene Testa