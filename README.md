**AEG: A Python framework for modeling of adaptive evolutionary games**


**Overview**

Adaptive evolutionary games (AEGs) extend classical evolutionary game theory by allowing players’ strategies to evolve 
through trait coevolution mediated by eco-evolutionary feedbacks.
AEG is an open-source Python framework for simulating trait-mediated and density-dependent interactions in multispecies 
systems. The framework models the coupled dynamics of population densities and continuous traits using a unified system of 
ordinary differential equations.
Unlike traditional evolutionary games, which assume fixed traits and static payoff matrices, AEG enables adaptive trait 
evolution that dynamically reshapes interaction payoffs over time. This allows researchers to study feedback-driven 
coevolutionary dynamics in complex adaptive ecological systems.

The software supports an arbitrary number of interacting players, facilitating the analysis of:

- Multiplayer coevolutionary dynamics
- Payoff matrix
- Eco-evolutionary feedbacks
- Stability and bifurcation behavior
- Trait-mediated interaction shifts

AEG is designed to provide a transparent and reproducible computational workflow for evolutionary and theoretical ecology 
research.

**Key Features**
- Unified ODE-based modeling of density-trait dynamics
- Continuous trait evolution
- Density-dependent and trait-mediated interactions
- Arbitrary number of interacting species/strategies
- Vectorized implementation for computational efficiency
- Integration with modern numerical solvers
- Reproducible simulation workflow

**Mathematical Framework**

AEG models eco-evolutionary systems as coupled ordinary differential equations of the general form:
- Population density dynamics
- Trait evolutionary dynamics

The framework allows flexible specification of interaction functions and payoff structures, enabling users to define custom 
adaptive evolutionary games while maintaining a consistent computational backbone.

**Installation requirements** 
- Python 3.9+
- NumPy
- SciPy
- Matplotlib
- Jupyter Notebook

**Install dependencies**
- pip install -r requirements.txt

**Clone the repository**
- git clone https://github.com/Mmatlouk/AEG.git
- cd AEG

**Usage**
To reproduce simulations and figures
- jupyter notebook amg.ipynb

Run all cells sequentially to generate:
- Trait evolution trajectories
- Population density dynamics

**Reproducibility**

AEG is implemented using vectorized operations and modern numerical solvers to ensure:
- Deterministic reproducibility
- Transparent model specification
- Scalable simulations for multispecies systems

All results reported in the accompanying publication can be reproduced directly from the provided notebook and parameter configurations.

**License** 
- This project is licensed under the MIT License.

**Citation**
- If you use AEG in your research, please cite:
