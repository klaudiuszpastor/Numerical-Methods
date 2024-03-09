import numpy as np
import matplotlib.pyplot as plt


def wykres(a,b,x1,x2):
    x = np.linspace(x1, x2, 100)  # Przykładowy zakres od x1 do x2 z 100 punktami
    y = a * (x - b)**2
    plt.plot(x, y)
    plt.title('Wykres funkcji kwadratowej y = a * (x - b)^2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

wykres(2,4,0,10)

y1 = np.arange(1.0,5.0,0.01) #Trzeci argument jako podanie kroku
y2 = np.linspace(1.0,5.0,400) #Trzeci argument określa liczbę punktów

print(y1)
print(y2)