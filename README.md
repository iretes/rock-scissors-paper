# Rock, Scissors, Paper: the survival of the weakest 🪨✂️📄

A simulation of an agent-based model built with the [Mesa](https://mesa.readthedocs.io/en/stable/) framework.
It models a system with three species in a competitive loop: a rock beats (and replicates into) a pair of scissors, scissors beat a sheet of paper and paper beats a rock.

# How to install

To install the dependencies, execute the following command:

```bash
pip install -r requirements.txt
```

## How to run

To interactively run the model with agents activating simultaneously, execute the following command:

```bash
python ./run_simultaneous_act.py
```

To interactively run the model with agents activating sequentially, execute the following command:

```bash
python ./run_random_act.py
```

Then open your browser to http://127.0.0.1:8521/.

## Demo

![Demo](./demo.gif)

## References
- Frean, Marcus, and Edward R. Abraham. "Rock–scissors–paper and the survival of the weakest." Proceedings of the Royal Society of London. Series B: Biological Sciences 268.1474 (2001): 1323-1327.