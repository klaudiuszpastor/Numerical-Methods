import numpy as np
import matplotlib.pyplot as plt
# import scipy as sc

x=np.arange(1.0,5.0,0.01)
# y=np.cos(2*sc.pi*x)
 uzyskać dostęp do atrybutu "pi"
# w module "scipy", który nie istnieje
# Stała pi jest zwykle dostępna w module matematycznym lub numpy
y=np.cos(2*np.pi*x)
line=plt.plot(x,y,lw=2)
plt.ylim(y.min(),y.max())
plt.show()
