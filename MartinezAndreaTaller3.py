import numpy as np
import matplotlib.pylab as plt

a= 0.1
b=1
N=10000
h=(b-a)/(N-1.0)


x=np.linspace(-1,1,N)
def funcion(x):
	return (1.0/8.0)*((35*x**4)-(30*x**2)+(3))

plt.plot(x,funcion(x))
plt.show()

def IntTrap(x):

	inte1= np.sum( (h/2)*(funcion(x)[0]) + (h/2)*(funcion(x)[-1]))
	inte2= np.sum(h*funcion(x)[1:-1])
	intetra= (inte1+inte2)

	return intetra
y= IntTrap(x)

print "integral excata es es ",y

Np=100000

fne=[]
fpo=[]
for i in range (len(x)):
	
	if (funcion(x)[i]<0.0):
		fne.append(funcion(x)[i])
		
	elif(funcion(x)[i]>0.0):
		fpo.append(funcion(x)[i])


		
	

