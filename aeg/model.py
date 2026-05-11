import sympy as sp
import numpy as np

# ------------------------------------------------------------
# Symbolic Definitions
# ------------------------------------------------------------

# Trait interaction variables
dx_sym, dy_sym, sa_sym = sp.symbols('dx dy sa')

# Gaussian interaction kernel
G_sym = sp.exp(-(dx_sym**2 + dy_sym**2) / sa_sym**2)

# Automatic symbolic derivatives
dGdx_sym = sp.diff(G_sym, dx_sym)
dGdy_sym = sp.diff(G_sym, dy_sym)

# Convert symbolic expressions to numerical NumPy functions
G_func = sp.lambdify((dx_sym, dy_sym, sa_sym), G_sym, 'numpy')
dGdx_func = sp.lambdify((dx_sym, dy_sym, sa_sym), dGdx_sym, 'numpy')
dGdy_func = sp.lambdify((dx_sym, dy_sym, sa_sym), dGdy_sym, 'numpy')

# ------------------------------------------------------------
# Symbolic Growth Function
# ------------------------------------------------------------

x_sym, y_sym, xopt_sym, yopt_sym, sr_sym = sp.symbols('x y xopt yopt sr')

# Trait-dependent growth kernel
rxy_sym = sp.exp(-((x_sym - xopt_sym)**2 + (y_sym - yopt_sym)**2) / sr_sym**2)

# Automatic symbolic derivatives
drdx_sym = sp.diff(rxy_sym, x_sym)
drdy_sym = sp.diff(rxy_sym, y_sym)

# Convert to numerical functions
rxy_func = sp.lambdify((x_sym, y_sym, xopt_sym, yopt_sym, sr_sym), rxy_sym, 'numpy')

drdx_func = sp.lambdify((x_sym, y_sym, xopt_sym, yopt_sym, sr_sym), drdx_sym, 'numpy')

drdy_func = sp.lambdify((x_sym, y_sym, xopt_sym, yopt_sym, sr_sym), drdy_sym, 'numpy')

# ------------------------------------------------------------
# Adaptive Evolutionary Game
# ------------------------------------------------------------

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
    # Extract variables
    n = Y[:s]
    x = Y[s:2*s]
    y = Y[2*s:3*s]

    # Prevent negative densities
    n = np.maximum(n, 0)

    # Payoff/interaction matrix, e.g., cyclic dominance
    A = np.zeros((s, s))
    for i in range(s):
        A[i, (i+1) % s] = a
        A[i, (i-1) % s] = -a

    # Trait-dependent growth
    rxy = rxy_func(x, y, x_opt, y_opt, sr)

    # Numerical growth derivatives
    drdx = drdx_func(x, y, x_opt, y_opt, sr)
    drdy = drdy_func(x, y, x_opt, y_opt, sr)

    # Pairwise trait distances
    dx = x[:, None] - x[None, :]
    dy = y[:, None] - y[None, :]

    # Interaction kernels
    G = G_func(dx, dy, sa)

    # Automatic kernel derivatives
    dGdx = dGdx_func(dx, dy, sa)
    dGdy = dGdy_func(dx, dy, sa)

    # Trait-modified interaction matrix
    Axy = A * G
    interaction = Axy @ n

    # Ecological dynamics
    dotn = n * (r * rxy - n + interaction)

    # Selection gradients
    dAxy_dx = A * dGdx
    dAxy_dy = A * dGdy

    sx = (dAxy_dx @ n) + r * drdx
    sy = (dAxy_dy @ n) + r * drdy
    
    # Trait evolution
    dotx = ux * (n * sx)
    doty = uy * (n * sy)

    return np.concatenate([dotn, dotx, doty])