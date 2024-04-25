import numpy as np

# Dane wejściowe
A = np.array([[6, 2, 8],
              [3, 5, 2],
              [2, 8, 2]])
y = np.array([26, 18, 1])

x = np.linalg.solve(A, y)

print("Rozwiązanie macierzowe =", x)
print("-----------------------")

def metoda_iteracyjna(mA, my, x):
    n = len(mA)
    for j in range(0, n):
        yj = my[j]
        suma = 0
        for i in range(0, n):
            if j != i:
                suma += mA[j][i] * x[i]
        x[j] = (yj - suma) / mA[j][j]
    return x

x0 = np.array([0., 0., 0.])
e = 1  # początkowa wartość błędu
tolerancja = 0.01  # tolerancja błędu (1%)

# iteracja aż do osiągnięcia błędu mneijszego niż zdefiniowana tolerancja
# w każdej iteracji aktualizujemy przybliżenie x, obliczamy błąd i sprawdzamy 
# warunek stopu
iteracja = 0
while e > tolerancja:
    xi = metoda_iteracyjna(A, y, x0.copy())
    e = np.linalg.norm(x - xi) / np.linalg.norm(x)
    print("Rozwiązanie iteracyjne [", iteracja, "] =", xi)
    print("Błąd [", iteracja, "] =", e)
    x0 = xi[:]
    iteracja += 1

print("Liczba iteracji:", iteracja)
