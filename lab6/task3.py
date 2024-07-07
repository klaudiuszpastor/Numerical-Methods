import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor

# Define the custom neural network class
class NeuralNetwork:
    # ReLU activation function
    activ = lambda self, x: (x + abs(x)) / 2
    # Uncomment the following line to use Sigmoid activation function
    # activ = lambda self, x: 1 / (1 + np.exp(-x))

    def __init__(self, nodes, layers):
        self.L = nodes
        self.M = layers
        self.N = self.L + 2
        if layers == 1:
            self.N = 2

        self.xij = np.zeros(self.L * self.M).reshape((self.L, self.M))
        self.wij = np.zeros(self.L * self.N).reshape((self.L, self.N))

    def get_weights(self):
        return self.wij

    def set_weights(self, w):
        self.wij = w.copy()

    def randomize_weights(self):
        for i in range(self.L):
            for j in range(self.N):
                self.wij[i, j] = random.random() / 2  # Random weights [0.:0.5]

    def compute(self, x):
        self.xij[:, 0] = [self.activ(self.wij[i, 0] * x) for i in range(self.L)]
        for k in range(1, self.M):
            for j in range(1, self.N):
                for i in range(self.L):
                    self.xij[i, k] = sum([self.activ(self.wij[i, j] * xi) for xi in self.xij[:, k - 1]])
        y = sum([self.activ(self.wij[i, self.N - 1] * self.xij[i, self.M - 1]) for i in range(self.L)])
        return y

    def mse(self, f, x_val):
        return (f(x_val) - self.compute(x_val)) ** 2

# Function to be approximated
f = lambda x: x ** 2

# Initialize custom neural network
nn = NeuralNetwork(10, 2)  # 10 nodes and 2 hidden layers
x = 1.0
nn.randomize_weights()

# Training custom neural network
min_mse = np.inf
optimal_weights = None

for _ in range(1000):
    nn.randomize_weights()
    mse_val = nn.mse(f, x)
    if mse_val < min_mse:
        min_mse = mse_val
        optimal_weights = nn.get_weights().copy()

nn.set_weights(optimal_weights)

print("Training completed")
print(f"For x = {x}, f(x) = {f(x)}")
print(f"For x = {x} and randomized weights, NN(x) = {nn.compute(x)}")
print(f"MSE Error: {(f(x) - nn.compute(x)) ** 2}")

# Comparison with MLPRegressor
x_data = np.linspace(0, 1, 10)
y_data = f(x_data)

x_data_set = x_data[:, np.newaxis]
y_data_set = y_data

mplr = MLPRegressor(hidden_layer_sizes=(100,), activation='identity', max_iter=1000)
mplr.fit(x_data_set, y_data_set)
y_predicted = mplr.predict(x_data_set)

print(f"MLPRegressor Score: {mplr.score(x_data_set, y_data_set)}")

# Plot results
plt.plot(x_data, y_data, label='Function')
plt.plot(x_data, y_predicted, label='MLPRegressor')
plt.plot(x_data, [nn.compute(x) for x in x_data], label="Custom Network")
plt.legend()
plt.show()
