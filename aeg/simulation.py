import numpy as np
from scipy.integrate import solve_ivp
from .model import adaptive_game


def run_simulation(s, seed=1,
                   a=1.0, r=1.0,
                   sa=0.3, sr=0.5,
                   mutation_rate1=0.02, mutation_rate2=0.03,
                   t_max=400,
                   n_points=10000):

    np.random.seed(seed)

    ux = np.ones(s) * mutation_rate1
    uy = np.ones(s) * mutation_rate2

    x_opt = np.random.rand(s)
    y_opt = np.random.rand(s)

    n0 = np.random.rand(s)
    x0 = np.random.rand(s)
    y0 = np.random.rand(s)
    Y0 = np.concatenate([n0, x0, y0])

    t_span = (0, t_max)
    t_eval = np.linspace(0, t_max, n_points)

    sol = solve_ivp(
        adaptive_game,
        t_span,
        Y0,
        args=(s, a, r, sa, sr, ux, uy, x_opt, y_opt),
        t_eval=t_eval,
        method='RK45',
        rtol=1e-6,
        atol=1e-9
    )

    n = sol.y[:s]
    x = sol.y[s:2*s]
    y = sol.y[2*s:3*s]

    return t_eval, n, x, y
