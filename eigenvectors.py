import numpy as np
import matplotlib.pyplot as plt


m1 = np.zeros((100,100),dtype=float)
3
m1[0][0]=-1
m1[0][1]=0.5
m1[0][-1]=0.5

m1[-1][-1]=-1
m1[-1][-2]=0.5
m1[-1][0]=0.5

i=0
for item in m1[1:m1.shape[0]-1]:
	item[i+1] = -1
	item[i+2] = item[i] = 0.5
	i=i+1

#print(m1)

x = np.linalg.eig(m1)
#print('np.linalg.eig(m1)\n',x)

eigenvalues = x[0]
eigenvectors = x[1]

#print('eigenvalues\n',eigenvalues)
#print('eigenvectors\n',eigenvectors)

plt.plot(eigenvectors[:,40])
#plt.plot(eigenvectors[:,10])

for ev in range(0,100):
	print(ev,eigenvalues[ev])


plt.show()