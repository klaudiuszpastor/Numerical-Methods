import numpy as np
import matplotlib.pyplot as plt

# Definiujemy współczynniki a i b
a = 2
b = 3

# Tworzymy zakres zmiennej niezależnej x
x = np.linspace(0, 10, 100)  # Przykładowy zakres od 0 do 10 z 100 punktami

# Obliczamy wartości funkcji kwadratowej y
y = a * (x - b)**2

# Tworzymy wykres
plt.plot(x, y)
plt.title('Wykres funkcji kwadratowej y = a * (x - b)^2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
