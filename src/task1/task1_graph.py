import numpy as np
import matplotlib.pyplot as plt

x_left = np.linspace(0, 0.999, 500)   
x_right = np.linspace(1.001, 8, 500) 

x = np.concatenate([x_left, x_right])

y = (x**2 + 1) / (x - 1)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2)

plt.title('График функции $y = \\frac{x^2 + 1}{x - 1}$', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

plt.xlim(0, 2)
plt.ylim(-100, 100)


plt.axvline(x=1, color='r', linestyle='--', alpha=0.5, label='x=1 (вертикальная асимптота)')
plt.legend()

plt.savefig("task1_graph.png", dpi=600, bbox_inches='tight')
