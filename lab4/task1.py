# Korzystając z algorytmu dla metody bisekcji, napisz program do poszukiwania miejsc
# zerowych równań funkcyjnych opisanych zależnością y=f(x)=0, a następnie narysuj
# wykres funkcji f(x) i zaznacz na wykresie znalezione rozwiązania.
# https://en.wikipedia.org/wiki/Bisection_method

import numpy as np
import matplotlib.pyplot as plt
from math import *

def bisekcja(f, a, b,tol=1e-6,max_iter=100):
    # tol - tolerancja - maksymalną dopuszczalną wartośc błędu
    # max_iter - maksymalna liczba iteracji, które algorytm może wykonać w poszukiwaniu miejsca zerowego
    if f(a) * f(b) > 0:
        print("Brak zmiany znaku funkcji")
        return None

    i = 0
    while i < max_iter:
        c = (a + b) / 2
        if f(c) == 0 or (b-a)/2 < tol:
            return c
        elif f(a) * f(c) <0:
            b = c
        else:
            a = c
        i += 1
    
def wykres(funkcja, a, b):
    # Funkcja lambda do ewaluacji funkcji na podstawie tekstu
    f = lambda x: eval(funkcja, globals(), locals())
    
    x = np.linspace(a, b, 1000)
    y = f(x)
    plt.plot(x, y, label="f(x)")
    
    # Znalezienie miejsc zerowych
    roots = [] # przechowywanie wszystkich miejsc zerowych
    x_values = np.linspace(a, b, 1000) # rozmieszczenie wartości w zakresie a do b
    for i in range(len(x_values) - 1):
        if f(x_values[i]) * f(x_values[i + 1]) <= 0: # sprawdza, czy wartości funkcji na dwóch kolejnych punktach mają przeciwne
                                                     # znaki - jeśli tak to między nimi znajduje się miejsce zerowe
            root = bisekcja(f, x_values[i], x_values[i + 1]) # dokładne miejsce zerowe między tymi dwoma punktami
            roots.append(root)
    
    # Narysowanie linii poziomych dla miejsc zerowych
    for root in roots:
        plt.axhline(0, color='red', linestyle='--')
        plt.scatter(root, 0, color='red')
        print("x=",root) # Wyświetlenie tych miejsc zerowych
        print("f(x)=", f(root)) # Wyświetlenie wartości funkcji
    
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Wykres funkcji f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Zakres osi x
x_min = -2
x_max = 2

funkcja = '2*x**2-4*np.sin(x)+np.exp(x)-5'
# Rysowanie wykresu
wykres(funkcja, x_min, x_max)

