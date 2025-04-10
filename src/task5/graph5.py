import numpy as np
from scipy.integrate import quad

# Параметризация кривой: x = t, y = 2/(12t)^(1/3), z = (12t)^(1/3)
def curve_derivatives(t):
    dx_dt = 1  # Производная x по t
    
    # Производная y по t (используем цепное правило)
    dy_dt = -2/3 * (12*t)**(-4/3) * 12  # = -8 / (12t)^(4/3)
    
    # Производная z по t
    dz_dt = (1/3) * (12*t)**(-2/3) * 12  # = 4 / (12t)^(2/3)
    
    return dx_dt, dy_dt, dz_dt

# Функция для подынтегрального выражения (модуль скорости)
def integrand(t):
    dx, dy, dz = curve_derivatives(t)
    return np.sqrt(dx**2 + dy**2 + dz**2)

# Вычисляем длину кривой от t_min до t_max
t_min = 2/3
t_max = 18
length, error = quad(integrand, t_min, t_max)

print(f"Длина кривой: {length:.5f}")
print(f"Погрешность вычисления: {error:.5e}")