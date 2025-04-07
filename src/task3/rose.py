import numpy as np
import matplotlib.pyplot as plt

# Настройки стиля
plt.style.use('seaborn-v0_8')

# Параметры розы
a = 1
t = np.linspace(0, 2*np.pi, 1000)

# Координаты розы (полярные -> декартовы)
r = a * np.sin(4*t)
x_rose = r * np.cos(t)
y_rose = r * np.sin(t)

# Стебель (вертикальная линия + листья)
x_stem = [0, 0]
y_stem = [-2, -0.2]

# Листья стебля (параболы)
x_leaf = np.linspace(-0.5, 0.5, 50)
y_leaf_left = 0.3*(x_leaf+0.3)**2 - 1.5
y_leaf_right = 0.3*(x_leaf-0.3)**2 - 1.2

# Создание фигуры
fig, ax = plt.subplots(figsize=(8, 10))

# Рисуем розу с градиентной заливкой
for i in range(8):
    segment = slice(i*125, (i+1)*125)
    ax.fill(x_rose[segment], y_rose[segment], 
            color=plt.cm.viridis(i/8), alpha=0.7, edgecolor='black', lw=1)

# Рисуем стебель
ax.plot(x_stem, y_stem, 'g-', linewidth=4, alpha=0.7)

# Рисуем листья
ax.fill_between(x_leaf, y_leaf_left, -2, color='green', alpha=0.3)
ax.fill_between(x_leaf, y_leaf_right, -2, color='green', alpha=0.3)

# Декоративные элементы
ax.set_title("8-лепестковая роза\n$r = a\cdot\sin(4\\theta)$", fontsize=16, pad=20)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-2, 1.5)
ax.set_aspect('equal')
ax.axis('off')  # Скрываем оси

# Добавляем текст с формулой
ax.text(0, -1.8, r"$x = a\sin(4t)\cos(t)$"+"\n"+r"$y = a\sin(4t)\sin(t)$", 
        ha='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout()
plt.savefig("rose.png", dpi=600)