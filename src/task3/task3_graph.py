import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 1000)
a = 1
x = a * np.sin(4*t)
y = a * np.sin(t)

plt.plot(x, y)
plt.title('График x = a sin(4t), y = a sin(t)')
plt.grid()
plt.savefig("task3_graph.png", dpi=600)