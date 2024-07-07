import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize, LinearConstraint, Bounds, dual_annealing, differential_evolution

# Define the objective function and the Trajectory class
def fun(x):
    return (x[0] - 5)**2 + (x[1] - 8)**2 + 100

class Trajectory:
    def __init__(self):
        self._fun = None
        self._trace_points = None

    def _objective_function(self, x, *args):
        res = self._fun(x)
        self._trace_points.append(x)
        return res

    def minimalize_simplex(self, fun, x0):
        self._trace_points = []
        self._fun = fun
        return minimize(self._objective_function, x0, method='Nelder-Mead')

    def minimalize_gradient(self, fun, x0):
        self._trace_points = []
        self._fun = fun
        return minimize(self._objective_function, x0, method='CG')

    def minimalize_annealing(self, fun, bounds):
        self._trace_points = []
        self._fun = fun
        return dual_annealing(self._objective_function, bounds)

    def minimalize_evolution(self, fun, bounds):
        self._trace_points = []
        self._fun = fun
        return differential_evolution(self._objective_function, bounds)

    def get_trace_points(self):
        return np.row_stack(self._trace_points)

# Define the 2D contour plotting function with gradient paths
def plot_contour_with_paths(ax, fun, x1, x2, trace, title):
    x, y = np.meshgrid(x1, x2)
    z = np.array([fun([x[i, j], y[i, j]]) for i in range(x.shape[0]) for j in range(x.shape[1])]).reshape(x.shape)
    ax.contour(x, y, z, levels=20)
    trace = np.array(trace)
    ax.plot(trace[:, 0], trace[:, 1], 'ro-')
    ax.quiver(trace[:-1, 0], trace[:-1, 1], trace[1:, 0] - trace[:-1, 0], trace[1:, 1] - trace[:-1, 1], angles='xy', scale_units='xy', scale=1, color='r')
    ax.set_title(title)

# Initialize the variables
lb = [-100, -100]
ub = [100, 100]
x = np.arange(lb[0], ub[0], 1)
y = np.arange(lb[1], ub[1], 1)
tr = Trajectory()

# Perform the optimization for Simplex and Gradient methods
out_simplex = tr.minimalize_simplex(fun, [100, 100])
trace_simplex = tr.get_trace_points().copy()

out_gradient = tr.minimalize_gradient(fun, [100, 100])
trace_gradient = tr.get_trace_points().copy()

# Create figure for 2D contour plots with gradient paths
fig_2d, axs_2d = plt.subplots(1, 2, figsize=(12, 6))
fig_2d.subplots_adjust(hspace=0.3, wspace=0.3)

# Plot 2D contour plots for Simplex and Gradient methods
plot_contour_with_paths(axs_2d[0], fun, x, y, trace_simplex, "Simplex 2D")
plot_contour_with_paths(axs_2d[1], fun, x, y, trace_gradient, "Gradient 2D")

plt.show()

print("Simplex result:", out_simplex.x)
print("Gradient result:", out_gradient.x)
