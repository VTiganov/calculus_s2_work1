import numpy as np
import matplotlib.pyplot as plt

# Определяем функцию
def f(x):
    return x / (x + 2)

# Создаем данные для графика
x = np.linspace(-1.5, 1.5, 400)
y = f(x)

# Область интегрирования
x_fill = np.linspace(-1, 1, 100)
y_fill = f(x_fill)

# Создаем график
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r'$f(x) = \frac{x}{x+2}$', linewidth=2)
plt.fill_between(x_fill, y_fill, alpha=0.3, label='Область интегрирования [-1,1]')

# Настраиваем отображение
plt.title('График функции с областью интегрирования')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

# Сохраняем график
plt.savefig('integral_plot.png', dpi=300)
plt.show()