import numpy as np
import matplotlib.pyplot as plt
"""
def f(x):
    return np.piecewise(x,[(x < 0), (0 < x) ],[lambda x: 5*np.cos(x*x-x), lambda x: x*x+3*x+5, 0])

x = np.linspace(-4, 4, 400)
y = f(x)
"""
def f(x):
    return np.exp(x)-np.log(x+1)*np.cos(x)-2
"""
x = np.linspace(-2,2,400)
y = f(x)

plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.plot(x, y)
plt.show()

"""

x = -5
for i in range(50):
    x1= x+0.5 * i
    x2= x1*0.5
    if (f(x1)*f(x2)<0):
        print (f'[{x1},{x2}] hay un 0 real')

