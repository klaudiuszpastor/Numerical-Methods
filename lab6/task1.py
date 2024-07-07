import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize, LinearConstraint, Bounds

def target_function(variables):
    value = variables[0] * 5 * 30 + variables[1] * 4 * 50 - (5 * variables[0] + 10 * variables[1]) * 10
    return -value

bounds = Bounds([0, 0], [50, 30])
constraints = LinearConstraint([[1, 1], [5, 10]], [0, 0], [60, 400])

optimal_result = minimize(target_function, [25, 15], method='SLSQP', bounds=bounds, constraints=constraints)

def plot(func, x_range, y_range, optimal_points, plot_title):
    x, y = np.meshgrid(x_range, y_range)
    z = np.array([func([x[i, j], y[i, j]]) for i in range(x.shape[0]) for j in range(x.shape[1])]).reshape(x.shape)
    z_optimal = np.array([func([optimal_points[i, 0], optimal_points[i, 1]]) for i in range(optimal_points.shape[0])])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title(plot_title)
    ax.plot_surface(x, y, z, alpha=0.7, cmap='viridis')
    ax.scatter(optimal_points[:, 0], optimal_points[:, 1], z_optimal, color='red', s=50)
    plt.show()

x_range = np.arange(0, 50, 1)
y_range = np.arange(0, 30, 1)

print(f"Optimal variables: {optimal_result.x}")
print(f"Optimal function value: {-optimal_result.fun}")
print(f"Optimization success: {optimal_result.success}")
print(f"Optimization status: {optimal_result.message}")

plot(target_function, x_range, y_range, np.array([optimal_result.x]), "Optimization Result")

