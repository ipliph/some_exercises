import matplotlib.pyplot as plt
from scipy import integrate
import math
import numpy as np

x_values = np.arange(0.,math.sqrt(2*math.pi),0.01)

y_values = np.square(np.sin(np.square(x_values)))

plt.plot(x_values,y_values)

func = lambda x: math.pow(math.sin(x*x),2)

int_value = integrate.quad(func,0,math.sqrt(2*math.pi))
print('Integrate value equals ',int_value[0],' and estimate of the absolute error equals ',int_value[1],'.')

plt.show()