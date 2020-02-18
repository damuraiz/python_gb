# Постройте на одном графике две кривые y(x) для функции двух переменной y(k,x)=cos(k∙x),
# взяв для одной кривой значение k=1, а для другой – любое другое k, не равное 1.


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 200)
fx1=np.cos(x)
fx2=np.cos(2*x)
plt.plot(x, fx1)
plt.plot(x, fx2)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
