import numpy as np


def adaptive_game(t, Y, s, a, r, sa, sr, ux, uy, x_opt, y_opt):
    """
    Core adaptive evolutionary game dynamics.

    Parameters
    ----------
    t : float
        Time variable.
    Y : ndarray
        State vector (densities and traits).
    s : int
        Number of strategies.
    a : float
        Maximum payoff magnitude.
    r : float
        Maximum intrinsic growth rate.
    sa : float
        Width of Gaussian payoff kernel.
    sr : float
        Width of Gaussian growth kernel.
    ux, uy : ndarray
        Mutation rates.
    x_opt, y_opt : ndarray
        Optimal trait values.
    """

    n = Y[:s]
    x = Y[s:2*s]
    y = Y[2*s:3*s]

    n = np.maximum(n, 0)

    # Flexible payoff matrix structures enabling multiple interaction types. E.g., Cyclic dominance matrix
    A = np.zeros((s, s))
    for i in range(s):
        A[i, (i+1) % s] = a
        A[i, (i-1) % s] = -a

    rxy = np.exp(-((x - x_opt)**2 + (y - y_opt)**2) / sr**2)

    dx = x[:, None] - x[None, :]
    dy = y[:, None] - y[None, :]
    G = np.exp(-(dx**2 + dy**2) / sa**2)

    Axy = A * G
    interaction = Axy @ n

    dotn = n * (r * rxy - n + interaction)

    dGdx = G * (-2 * dx / sa**2)
    dGdy = G * (-2 * dy / sa**2)

    dAxy_dx = A * dGdx
    dAxy_dy = A * dGdy

    sx = (dAxy_dx @ n) + r * (-2*(x - x_opt)/sr**2) * rxy
    sy = (dAxy_dy @ n) + r * (-2*(y - y_opt)/sr**2) * rxy

    dotx = ux * (n * sx)
    doty = uy * (n * sy)

    return np.concatenate([dotn, dotx, doty])