import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parametry
t = np.linspace(0, 4, 1000, endpoint=False)
tp = signal.square(np.pi * t)

# Funkcja do generowania sumy funkcji trygonometrycznych
def suma_trygonometrycznych(t, N):
    suma = np.zeros_like(t)
    for n in range(1, N+1):
        if n % 2 != 0:  # tylko nieparzyste harmoniczne
            suma += (4 / (np.pi * n)) * np.sin(n * np.pi * t)
    return suma

# Liczba składników trygonometrycznych
N = 5
ts = suma_trygonometrycznych(t, N)

# Wykres
plt.figure(figsize=(10, 6))
plt.plot(t, tp, label='Sygnał prostokątny')
plt.plot(t, ts, label=f'Suma {N} funkcji trygonometrycznych')
plt.xlabel('t')
plt.ylabel('Amplituda')
plt.legend(loc="upper right")
plt.title('Dopasowanie sygnału prostokątnego')
plt.grid(True)
plt.show()

# Estymacja dokładności dopasowania
def oszacuj_dokladnosc(t, tp, N):
    ts = suma_trygonometrycznych(t, N)
    blad = np.mean((tp - ts) ** 2)
    return blad

# Przykładowa ocena dla kilku wartości N
for N in [1, 3, 5, 7, 9, 11, 15, 20]:
    blad = oszacuj_dokladnosc(t, tp, N)
    print(f'N = {N}, Średni kwadratowy błąd: {blad}')
