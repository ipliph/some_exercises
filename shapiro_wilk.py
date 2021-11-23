import matplotlib.pyplot as plt
from scipy import stats
import numpy as np


data1 = np.random.normal(3,9,10)
dest1 = '\n\nsample drawn from the normal distribution N(3,9) for N=10'

data2 = np.random.normal(3,9,50)
dest2 = '\n\nsample drawn from the normal distribution N(3,9) for N=50'

data3 = np.random.uniform(-1.5,1.5,10)
dest3 = '\n\nsample drawn from the uniform distribution [-1.5,1.5] for N=10'

data4 = np.random.uniform(-1.5,1.5,100)
dest4 = '\n\nsample drawn from the uniform distribution [-1.5,1.5] for N=100'

data5 = np.random.uniform(-10,10,10)
dest5 = '\n\nsample drawn from the uniform distribution [-10,10] for N=10'

data6 = np.random.uniform(-10,10,100)
dest6 = '\n\nsample drawn from the uniform distribution [-10,10] for N=100'

data7 = np.random.standard_t(1,size=10)
dest7 = '\n\nsample drawn from the t-Student distribution with number of degrees of freedom = 1'

data8 = np.random.standard_t(10,size=10)
dest8 = '\n\nsample drawn from the t-Student distribution with number of degrees of freedom = 10'

data9 = np.random.chisquare(3,size=10)
dest9 = '\n\nsample drawn from the Chi-2 distribution with number of degrees of freedom = 3'

def swtest(data,desc):
	print(desc)
	sw = stats.shapiro(data)
	print("sw : " , sw)
	print("sw.statistic : " , sw.statistic)
	print("sw.pvalue : " , sw.pvalue)
	#datanorm = stats.norm.rvs(size = 10000)
	#swnorm = stats.shapiro(datanorm)
	#print("swnorm : " , swnorm)
	#print("swnorm.statistic : " , swnorm.statistic)
	#print("swnorm.pvalue : " , swnorm.pvalue)
	#print('\n\n...END...')

swtest(data1,dest1)
swtest(data2,dest2)
swtest(data3,dest3)
swtest(data4,dest4)
swtest(data5,dest5)
swtest(data6,dest6)
swtest(data7,dest7)
swtest(data8,dest8)
swtest(data9,dest9)