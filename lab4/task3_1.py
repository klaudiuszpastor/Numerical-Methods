import numpy as np
import sympy as sp

# Definicja zmiennych symbolicznych
x1, x2 = sp.symbols('x1 x2')

# Definicja funkcji
F1 = x1 * x2 - 1
F2 = x1 + x2 - 2
F = sp.Matrix([F1, F2])

# Definicja Jacobianu
J = F.jacobian([x1, x2])

# Początkowe wartości i iteracja
x = np.array([-1, 2])  # Początkowe przybliżenie rozwiązania
tolerancja = 1e-6  # Tolerancja błędu
max_iteracji = 100  # Maksymalna liczba iteracji

for iteracja in range(max_iteracji):
    F_val = np.array([F1.subs({x1: x[0], x2: x[1]}), F2.subs({x1: x[0], x2: x[1]})], dtype=float)
    # Obliczenie wartości F1 i F2 dla aktualnego przybliżenia x. Korzystanie z metody subs()
    # do postawienia wartości x1 i x2 w miejsce symboli
    if np.linalg.norm(F_val) < tolerancja:
        break
    J_val = np.array(J.subs({x1: x[0], x2: x[1]}), dtype=float)
    # Obliczamy wartości macierzy Jacobiego J dla aktualnego przybliżenia x poprzez zastąpienie symboli x1 i x2
    delta = np.linalg.solve(J_val, -F_val)
    x = x + delta

print("Rozwiązanie iteracyjne:", x)
print("Liczba iteracji:", iteracja + 1)

# Rozwiązanie nieliniowego układu równań za pomocą nonlinsolve()
rozwiazanie_sym = sp.nonlinsolve([F1, F2], [x1, x2])
print("Rozwiązanie za pomocą nonlinsolve():", rozwiazanie_sym)
