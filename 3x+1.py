import matplotlib.pylab as plt
import matplotlib.pyplot
import numpy as np
matplotlib.pyplot.grid(visible=None, which='major',axis='both')


for a in (1, 10):               #3x+1 Problem
    while a != 1:
        print(a)
        if a % 2 == 0:
            a = a // 2
        else:
            a = (a * 3) + 1

x = np.linspace(1, 10)          #graphischer plot von a und x --> Zoom & Darstellung von Punkten in MAtplot
y = np.linspace(1, 10)

print(a)
plt.plot(x, y)
plt.show()