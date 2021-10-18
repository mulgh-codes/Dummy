import numpy as np
import matplotlib.pyplot as plt
X=np.arange(25)
Y=np.random.randn(25)
x1=0
y1=0
fig=plt.figure()
for i in range(0,10):
	#plt.ion()
	plt.clf()
	x1=x1+0.2
	y1=y1-0.2
	plt.scatter(X, Y, color='greem')
	plt.scatter(x1,y1, color='blue')
	plt.pause(0.2)
	
plt.show()

	
