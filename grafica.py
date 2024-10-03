import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from main import integral, limite_inferior, limite_superior

# Creamos un rango de valores x para graficar
x = np.linspace(0, 4, 100)
y = integral(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r'$(3x + 2) \cdot \frac{1}{3} \ln(16)$', color='blue')
plt.fill_between(x, y, where=(x >= limite_inferior) & (
    x <= limite_superior), color='lightblue', alpha=0.5, label='Área bajo la curva')

plt.title('Gráfica de la Integral')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(limite_inferior, color='red', lw=1,
            ls='--', label='Límite inferior (x=2)')
plt.axvline(limite_superior, color='green', lw=1,
            ls='--', label='Límite superior (x=3)')
plt.legend()
plt.grid()

plt.savefig('grafica_integral.png')
print("La gráfica se ha guardado como 'grafica_integral.png'.")
