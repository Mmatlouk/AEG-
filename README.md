# AEG: A Python framework for modeling of adaptive evolutionary games

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18864928.svg)](https://doi.org/10.5281/zenodo.18864928)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Overview

Adaptive evolutionary games (AEGs) extend classical evolutionary game theory by allowing players’ strategies to evolve through trait coevolution mediated by eco-evolutionary feedbacks. AEG is an open-source Python framework for simulating trait-mediated and density-dependent interactions in multispecies systems. The framework models the coupled dynamics of population densities and continuous traits using a unified system of ordinary differential equations. Unlike traditional evolutionary games, which assume fixed traits and static payoff matrices, AEG enables adaptive trait evolution that dynamically reshapes interaction payoffs over time. This allows researchers to study feedback-driven coevolutionary dynamics in complex adaptive ecological systems.

The framework supports an arbitrary number of interacting players, facilitating the analysis of:

- Multiplayer coevolutionary dynamics  
- Flexible payoff matrix structures enabling multiple interaction types (e.g., cyclic dominance, competition, predator–prey, mutualistic systems)  
- Eco-evolutionary feedbacks  
- System stability and dynamical transitions  
- Trait-mediated interaction shifts  

AEG is designed to provide a transparent and reproducible computational workflow for evolutionary and theoretical ecology research.

---

## Key Features

- Unified ODE-based modeling of density-trait dynamics  
- Continuous trait evolution  
- Density-dependent and trait-mediated interactions  
- Arbitrary number of interacting species/strategies  
- Vectorized implementation for computational efficiency  
- Integration with modern numerical solvers  
- Reproducible simulation workflow  

---

## Installation Requirements

- Python 3.9+  
- NumPy  
- SciPy  
- Matplotlib  
- Jupyter Notebook  

### Install dependencies

```bash
pip install -r requirements.txt
```

## Clone the repository

```bash
git clone https://github.com/Mmatlouk/AEG-.git
cd AEG
```

---

## Usage

### Import as a Python package

```python
from aeg import run_simulation

# Run a simulation with 5 interacting strategies
t, n, x, y = run_simulation(5)
```

### Reproduce notebook simulations

```bash
jupyter notebook aeg.ipynb
```

Run all cells sequentially to generate:
- Trait evolution trajectories
- Population density dynamics

---

## Reproducibility

AEG is implemented using vectorized operations and modern numerical solvers to ensure:

- Deterministic reproducibility
- Transparent model specification
- Scalable simulations for multispecies systems

All results reported in the accompanying publication can be reproduced directly from the provided notebook and parameter configurations.

---

## License

This project is licensed under the MIT License.

---

## Citation

If you use AEG in your research, please cite: Kubyana, M.S., Landi, P., Hui, C. (2026). AEG pipeline for adaptive evolutionary games. Version 1.0.0. Zenodo. DOI: 10.5281/zenodo.18864928

See CITATION.cff for the correct reference format, including DOI.
