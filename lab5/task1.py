import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Dane wejściowe
x = np.array([1, 2, 3])
y = np.array([1, 3, 8])

# Regresja liniowa - metoda analityczna
def regresja_liniowa(x, y):
    meanX = np.mean(x)
    meanY = np.mean(y)
    covXY = np.mean((x - meanX) * (y - meanY))
    varX = np.var(x)
    a = covXY / varX
    b = meanY - a * meanX
    return a, b

a, b = regresja_liniowa(x, y)
print(f"Regresja liniowa - metoda analityczna: a = {a}, b = {b}")

# Regresja liniowa - metoda optymalizacyjna
def blad(coef):
    a, b = coef
    blad = 0
    for i in range(len(x)):
        blad += (a * x[i] + b - y[i]) ** 2
    return blad

wynik = minimize(blad, x0=[0, 0], method='CG')
a_opt, b_opt = wynik.x
print(f"Regresja liniowa - metoda optymalizacyjna: a = {a_opt}, b = {b_opt}")

# Interpolacja - wielomian II rzędu
A = np.vstack([np.ones(len(x)), x, x**2]).T
a0, a1, a2 = np.linalg.solve(A.T @ A, A.T @ y)
print(f"Interpolacja - wielomian II rzędu: a0 = {a0}, a1 = {a1}, a2 = {a2}")

# Wykres
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='red', label='Punkty pomiarowe')

# Wykres regresji liniowej
y_reg_lin = a * x + b
plt.plot(x, y_reg_lin, label='Regresja liniowa (analityczna)', color='blue')

# Wykres regresji liniowej (optymalizacja)
y_reg_lin_opt = a_opt * x + b_opt
plt.plot(x, y_reg_lin_opt, label='Regresja liniowa (optymalizacja)', color='green')

# Wykres interpolacji wielomianem II rzędu
y_interp = a0 + a1 * x + a2 * x**2
plt.plot(x, y_interp, label='Interpolacja (wielomian II rzędu)', color='purple')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Dopasowanie funkcji do punktów pomiarowych')
plt.grid(True)
plt.show()
