from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

n = 200

ax1 = plt.subplot(2,2,1)
x1 = np.random.uniform(-0.8,0.8,n)
res = stats.probplot(x1, plot=plt)
ax1.set_title('uniform distribution in range the range -0,8 to 0,8')

ax1 = plt.subplot(2,2,2)
x1 = np.random.uniform(-3,3,n)
res = stats.probplot(x1, plot=plt)
ax1.set_title('uniform distribution in range the range -3 to 3')

ax1 = plt.subplot(2,2,3)
x1 = np.random.uniform(-15,15,n)
res = stats.probplot(x1, plot=plt)
ax1.set_title('uniform distribution in range the range -15 to 15')

plt.show()

ax1 = plt.subplot(2,2,1)
x1 = np.random.standard_t(3, size=n)
res = stats.probplot(x1, plot=plt)
ax1.set_title('t-Student distribution \nwith 3 degrees of freedom')

ax2 = plt.subplot(2,2,2)
x2 = np.random.standard_t(25, size=n)
res = stats.probplot(x2, plot=plt)
ax2.set_title('t-Student distribution \nwith 20 degrees of freedom')

plt.show()

ax1 = plt.subplot(2,2,1)
def weib(x,n,a):
    return (a / n) * (x / n)**(a - 1) * np.exp(-(x / n)**a)

x = np.arange(1,100.)/50
res = stats.probplot(weib(x, 1., 8.9)*1.5, plot=plt)
ax1.set_title('Weibull distribution with a=8.9(shape parameter), b=1.5(scale parameter)')

ax2 = plt.subplot(2,2,2)
res = stats.probplot(weib(x, 1., 1.5)*5, plot=plt)
ax2.set_title('Weibull distribution with a=1.5(shape parameter), b=5(scale parameter)')

plt.show()

a = 2
b = 1
k = 1

ax1 = plt.subplot(2,2,1)
x1 = np.random.normal(-a,b,30)
res = stats.probplot(x1, plot=plt)
ax1.set_title('a combination of two normal distributions N(-a,b)')

ax2 = plt.subplot(2,2,2)
x1 = np.random.normal(k*a,k*b,30)
res = stats.probplot(x1, plot=plt)
ax2.set_title('a combination of two normal distributions N(k1a,k2b')

plt.show()