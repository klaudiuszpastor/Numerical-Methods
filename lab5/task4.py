import numpy as np

# Definicja funkcji aktywacji sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Funkcja obliczająca błąd dopasowania
def oblicz_blad(y_pred, y_true):
    return np.sum((y_pred - y_true) ** 2)

# Zbiór uczący
X = np.array([[0.1, 0.4, 0.5], [0.2, 0.8, 0.5]])
Y = np.array([[0.2, 0.3], [0.4, 0.7]])

# Liczba prób
liczba_prob = 1000

# Inicjalizacja minimalnego błędu
minimalny_blad = float('inf')
najlepsze_w = None
najlepsze_b = None

# Procedura losowania
for _ in range(liczba_prob):
    # Losowe wartości wag i przesunięć z zakresu [-1, 1]
    W = np.random.uniform(-1, 1, (2, 3))
    b = np.random.uniform(-1, 1, 2)
    
    # Obliczanie wyjścia sieci neuronowej
    Z = np.dot(W, X.T) + b[:, np.newaxis]
    Y_pred = sigmoid(Z)
    
    # Obliczanie błędu
    blad = oblicz_blad(Y_pred, Y.T)
    
    # Aktualizacja najlepszych wag i przesunięć
    if blad < minimalny_blad:
        minimalny_blad = blad
        najlepsze_w = W
        najlepsze_b = b

# Wyniki
print("Najlepsze wartości wag (W):")
print(najlepsze_w)
print("Najlepsze wartości przesunięć (b):")
print(najlepsze_b)
print("Minimalny błąd dopasowania:")
print(minimalny_blad)
