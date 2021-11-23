import numpy as np 
import matplotlib.pyplot as plt
import math


x = np.arange(11)

fsin = np.sin(x)
fcos = np.cos(x)
fexp = np.exp(-x)

plt.plot(x, fsin, 'r',label='sin(x)')
plt.plot(x, fcos, 'g-^',label='cos(x)') 
plt.plot(x, fexp, 'b-o',label='exp(x)')
plt.legend()
plt.show()


x = np.random.random(100)
y = np.random.random(100)

for num in range(100):

	area = (x[num]+y[num])*100
	#Points present better on the plot after multiplication by 100
	test = False
	for t in range(1,361):
		#  angle from 1 to 360
		trygfun = [(lambda t: math.cos(t))(t),(lambda t: math.sin(t))(t)]
		#two spaces after a period
		if round(x[num],2) <= round(trygfun[0],2) and round(y[num],2) <= round(trygfun[1],2):
			# True if coordinates of the designated point are lesser or equal the set of values of trigonometric functions 
			test = True
	if test == True:
		plt.scatter(x[num],y[num],s=area, c='green')
	else:
		plt.scatter(x[num],y[num],s=area, c='red')


plt.show()

