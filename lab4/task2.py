# Zastosuj metodę iteracyjną (Gaussa-Seidela) do rozwiązywanie układów równań
# liniowych. Metoda iteracyjna jest stosowana zazwyczaj do układów równań rzędu >3 i
# wymaga definicji punktu startowego x0. W kolejnych iteracjach wyznaczane są
# rozwiązania dla poszczególnych xi i porównywane z założonym błędem całkowitym e. W
# ramach ćwiczenia oszacuj liczbę iteracji N konieczną do wyznaczenia rozwiązania z
# dokładnością równą, np. 1 %.
# https://pl.wikipedia.org/wiki/Metoda_Gaussa-Seidla

import numpy as np

# Dane wejściowe
A = np.array([[6, 2, 8],
              [3, 5, 2],
              [2, 8, 2]])
y = np.array([26, 18, 1])

x = np.linalg.solve(A,y)

print("Rozwiazanie macieczowe=",x)
print("-----------------------")

def metoda_iteracyjna(mA,my,x):
    n=len(mA)
    for j in range(0,n):
        yj = my[j]
        suma = 0
        for i in range(0,n):
            if(j!=i):
                suma += mA[j][i] * x[i]
        x[j] = (yj-suma) / mA[j][j]
    return x

x0 = np.array([0.,0.,0.])
xi = np.array([])
e=0
for i in range(0,10):
    xi = metoda_iteracyjna(A,y,x0.copy())
    print("Rozwiazanie iteracyjne [",i,"]=",xi)
    e = np.linalg.norm([])
    print("Blad [",i,"]=",e)
    x0=xi[:]