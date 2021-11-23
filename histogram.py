import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from math import sqrt
x = norm.rvs(0,1,size = 100)
y = norm.rvs(1,2,size = 100)
z = norm.rvs(2,3,size = 100)

f = 2*x + y - 3*z
print(f)

print(f.mean())
w = norm.pdf(f)

print(w)


fig, result = plt.subplots()
result.hist(f, density=True, histtype='bar', alpha=0.5)
xs = np.linspace(np.min(f),np.max(f),100)
result.plot(xs,norm.pdf(xs,f.mean(),f.std()))

plt.show()
