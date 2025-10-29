import matplotlib.pyplot as plt
import numpy as np

# Distribución discreta: dado justo
valores = [1,2,3,4,5,6]
probabilidades = [1/6]*6

plt.bar(valores, probabilidades)
plt.xlabel("Valor del dado")
plt.ylabel("Probabilidad")
plt.title("Distribución de probabilidad de un dado justo")
plt.show()

# Distribución continua: normal
x = np.linspace(-4, 4, 1000)
mu = 0
sigma = 1
pdf = (1/(sigma * np.sqrt(2*np.pi))) * np.exp(-0.5*((x-mu)/sigma)**2)

plt.plot(x, pdf)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Distribución normal estándar")
plt.show()
