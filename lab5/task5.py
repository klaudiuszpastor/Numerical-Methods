import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Funkcja generująca dane
def generuj_dane(a, b, N):
    x = np.linspace(-1, 1, N)
    y = a * x + b + np.random.randn(N)  # dodanie losowego szumu
    return x, y

# Parametry
a = 2.0
b = 3.0
N = 100

# Generowanie danych
x, y = generuj_dane(a, b, N)

# Regresja liniowa
slope, intercept, r_value, p_value, std_err = linregress(x, y)
print(f"Współczynnik kierunkowy (slope): {slope}")
print(f"Przecięcie z osią y (intercept): {intercept}")
print(f"Współczynnik determinacji (R^2): {r_value**2}")
print(f"Błąd standardowy: {std_err}")

# Wartości dopasowanej funkcji regresji
y_fit = slope * x + intercept

# Wykres
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='red', label='Dane generowane')
plt.plot(x, y_fit, label='Dopasowana funkcja regresji', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Dopasowanie regresji liniowej: y = {slope:.2f}x + {intercept:.2f}')
plt.legend()
plt.grid(True)
plt.show()
