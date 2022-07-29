import matplotlib.pylab as plt
import matplotlib.pyplot
import numpy as np
matplotlib.pyplot.grid(visible=None, which='major',axis='both')

x = np.linspace(-2*np.pi, 2*np.pi)
y = 2*x
#z = np.cos(x)

#grid(color='r', linestyle='-', linewidth=2)
plt.plot(x, y, x, z)
plt.show()