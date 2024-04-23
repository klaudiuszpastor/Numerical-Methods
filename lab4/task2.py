import numpy as np

# Dane wejściowe
a = np.array([[6.0, 2.0, 8.0],
              [3.0, 5.0, 2.0],
              [2.0, 8.0, 2.0]])
b = np.array([26.0, 18.0, 1.0])

# Normalizacja danych
max_value_a = np.max(np.abs(a))
max_value_b = np.max(np.abs(b))
a_normalized = a / max_value_a
b_normalized = b / max_value_b

# Definicja punktu startowego
x0 = np.ones_like(b_normalized)  # Wartość początkowa - jedynki

# Definicja dokładności
tolerance = 0.01  # 1%

# Definicja maksymalnej liczby iteracji
max_iter = 1000

# Metoda iteracyjna (Gaussa-Seidela)
def gauss_seidel(a, b, x0, tolerance, max_iter):
    n = len(a)
    x = np.copy(x0)
    x_new = np.copy(x0)
    for iteration in range(1, max_iter + 1):
        for i in range(n):
            sigma = 0
            for j in range(n):
                if j != i:
                    sigma += a[i][j] * x_new[j]
            x[i] = (b[i] - sigma) / a[i][i]
        if np.linalg.norm(x - x_new) / np.linalg.norm(x0) < tolerance:
            return x, iteration
        x_new = np.copy(x)
    return x, max_iter

# Wyznaczenie rozwiązania
solution, num_iterations = gauss_seidel(a_normalized, b_normalized, x0, tolerance, max_iter)

# Odnormalizacja rozwiązania
solution_original = solution * max_value_b

print("Rozwiązanie układu równań liniowych:", solution_original)
print("Liczba iteracji potrzebna do osiągnięcia dokładności 1%:", num_iterations)
