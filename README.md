# AEG: A Python framework for modeling adaptive evolutionary games

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18864928.svg)](https://doi.org/10.5281/zenodo.18864928)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Overview

Adaptive evolutionary games (AEGs) extend classical evolutionary game theory by allowing players’ strategies to evolve through trait coevolution mediated by eco-evolutionary feedbacks.

**AEG** is an open-source Python framework for simulating **trait-mediated and density-dependent interactions in multispecies systems**. The framework models the coupled dynamics of **population densities and continuous traits** using a unified system of ordinary differential equations.

Unlike traditional evolutionary games, which assume fixed traits and static payoff matrices, **AEG enables adaptive trait evolution that dynamically reshapes interaction payoffs over time**. This allows researchers to study feedback-driven coevolutionary dynamics in complex adaptive ecological systems.

The framework supports an **arbitrary number of interacting players**, facilitating the analysis of:

- Multiplayer coevolutionary dynamics
- Flexible payoff matrix structures enabling multiple interaction types
- Eco-evolutionary feedbacks
- System stability and dynamical transitions
- Trait-mediated interaction shifts

AEG is designed to provide a **transparent and reproducible computational workflow for evolutionary and theoretical ecology research**.

---

# Key Features

- Unified **ODE-based modeling** of density-trait dynamics
- **Continuous trait evolution** via adaptive dynamics
- **Density-dependent and trait-mediated interactions**
- Arbitrary number of interacting species or strategies
- **Vectorized implementation** for computational efficiency
- Integration with modern numerical solvers (`scipy.integrate`)
- **Fully reproducible simulation workflow**

---

# Mathematical Framework

AEG models eco-evolutionary systems as **coupled ordinary differential equations** describing:

### Population density dynamics

Species densities evolve according to density-dependent ecological interactions and trait-mediated payoffs.

### Trait evolutionary dynamics

Continuous traits evolve through selection gradients and mutation processes that couple ecological and evolutionary dynamics.

This framework allows flexible specification of **interaction kernels, payoff matrices, and evolutionary parameters**, enabling users to construct custom adaptive evolutionary games while maintaining a consistent computational backbone.

---

# Repository Structure

AEG/
│
├── aeg/ # Core Python module
│ ├── init.py
│ ├── model.py
│ └── simulation.py simulation.py # Core AEG simulation engine
│
├── aeg.ipynb # Example notebook demonstrating simulations
├── requirements.txt
├── CITATION.cff
├── LICENSE
└── README.md

---

# Installation

Clone the repository

git clone https://github.com/Mmatlouk/AEG-.git

cd AEG-

Install dependencies

pip install -r requirements.txt

Required packages:

- Python 3.9+
- NumPy
- SciPy
- Matplotlib
- Jupyter Notebook

---

# Usage

The easiest way to run the framework is through the provided notebook.

Start Jupyter:

jupyter notebook aeg.ipynb

Run all cells sequentially to generate:

- Population density dynamics
- Trait evolution trajectories
- Example simulations of adaptive multiplayer games

The notebook demonstrates how to use the **core simulation engine implemented in `aeg/simulation.py`.**

Run example:

from aeg import run_simulation

t, n, x, y = run_simulation(5)

---

# Reproducibility

AEG is implemented using **vectorized numerical operations and modern ODE solvers** to ensure:

- Deterministic reproducibility
- Transparent model specification
- Scalable simulations for multispecies systems

All results reported in the accompanying publication can be reproduced directly using the provided notebook and parameter configurations.

---

# License

This project is licensed under the **MIT License**.

---

# Citation

If you use **AEG** in your research, please cite:

Kubyana, M., Landi, P., & Hui, C. (2026).
AEG pipeline for adaptive evolutionary games (Version 1.0.0).
Zenodo. https://doi.org/10.5281/zenodo.18864928

You can also use the **CITATION.cff** file to automatically generate citations via GitHub.
