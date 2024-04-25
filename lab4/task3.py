# Zastosuj metodę iteracyjną do rozwiązywania nieliniowych układów równań. W tym celu
# skorzystaj z:
# • definicji Jacobianu → macierz pochodnych cząstkowych
# • rozwinięcia funkcji w szereg Taylora → dwa pierwsze wyrazy
# • symbolicznego wyznaczania pochodnej → np. biblioteka sympy
# • algorytmu rozwiązywania liniowych układów równań → np. solve(A,y)
# napisz kod do iteracyjnego wyznaczania rozwiązania dla układu równań nieliniowych 
import numpy as np
import sympy as sp

x = np.array([-1,2])
F1 = x[0] * x[1] -1
F2 = x[0] + x[1] -2
F = np.array([F1,F2])

J11 = x[1]
J12 = x[0]
J21 = 1
J22 = 1
J = np.array([[J11,J12],[J21,J22]])
delta = np.linalg.solve(J,-F)
x = x + delta

print("delta=",delta)
print("Pierwsza iteracja -> [x]=",x)

A = np.array([[1,2],[3,4]])
y =np.array([5,6])

numpy_x = np.linalg.solve(A,y)
print("numpy solution [x]=",numpy_x)
x1,x2 = sp.symbols('x1 x2')
sympy_x = sp.linsolve(sp.Matrix(([1,2,5],[3,4,6])),(x1,x2))
print("Sympy solution [x]=",sympy_x)
