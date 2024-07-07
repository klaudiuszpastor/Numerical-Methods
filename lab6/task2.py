import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize, dual_annealing, differential_evolution

# Objective function 
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

# 3D plotting 
def plot3d_combined(ax, fun, x1, x2, trace, title):
    x, y = np.meshgrid(x1, x2)
    z = np.array([fun([x[i, j], y[i, j]]) for i in range(x.shape[0]) for j in range(x.shape[1])]).reshape(x.shape)
    ax.plot_surface(x, y, z, alpha=0.7, cmap='viridis')
    trace = np.array(trace)
    ax.plot(trace[:, 0], trace[:, 1], np.array([fun(t) for t in trace]), 'ro-')
    ax.set_title(title)

# 2D contour plotting 
def plot_contour(ax, fun, x1, x2, trace, title):
    x, y = np.meshgrid(x1, x2)
    z = np.array([fun([x[i, j], y[i, j]]) for i in range(x.shape[0]) for j in range(x.shape[1])]).reshape(x.shape)
    ax.contour(x, y, z, levels=20)
    trace = np.array(trace)
    ax.plot(trace[:, 0], trace[:, 1], 'ro-')
    ax.set_title(title)

# Initialize the variables
lb = [-100, -100]
ub = [100, 100]
x = np.arange(lb[0], ub[0], 1)
y = np.arange(lb[1], ub[1], 1)
tr = Trajectory()

# Optimization for each method
out_simplex = tr.minimalize_simplex(fun, [100, 100])
trace_simplex = tr.get_trace_points().copy()

out_gradient = tr.minimalize_gradient(fun, [100, 100])
trace_gradient = tr.get_trace_points().copy()

out_annealing = tr.minimalize_annealing(fun, list(zip(lb, ub)))
trace_annealing = tr.get_trace_points().copy()

out_evolution = tr.minimalize_evolution(fun, list(zip(lb, ub)))
trace_evolution = tr.get_trace_points().copy()


print("Simplex result:", out_simplex.x)
print("Gradient result:", out_gradient.x)
print("Annealing result:", out_annealing.x)
print("Evolution result:", out_evolution.x)

# Figure for 3D plots
fig_3d, axs_3d = plt.subplots(2, 2, figsize=(12, 12), subplot_kw={'projection': '3d'})
fig_3d.subplots_adjust(hspace=0.3, wspace=0.3)

# Plot 3D plots for each method
plot3d_combined(axs_3d[0, 0], fun, x, y, trace_simplex, "Simplex 3D")
plot3d_combined(axs_3d[0, 1], fun, x, y, trace_gradient, "Gradient 3D")
plot3d_combined(axs_3d[1, 0], fun, x, y, trace_annealing, "Annealing 3D")
plot3d_combined(axs_3d[1, 1], fun, x, y, trace_evolution, "Evolution 3D")

plt.show()

# Figure for 2D contour plots
fig_2d, axs_2d = plt.subplots(2, 2, figsize=(12, 12))
fig_2d.subplots_adjust(hspace=0.3, wspace=0.3)

# Plot 2D contour plots for each method
plot_contour(axs_2d[0, 0], fun, x, y, trace_simplex, "Simplex 2D")
plot_contour(axs_2d[0, 1], fun, x, y, trace_gradient, "Gradient 2D")
plot_contour(axs_2d[1, 0], fun, x, y, trace_annealing, "Annealing 2D")
plot_contour(axs_2d[1, 1], fun, x, y, trace_evolution, "Evolution 2D")

plt.show()
