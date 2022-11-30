import math
import matplotlib.pyplot as plt
import mylibrary.rk4sho as sho
gamma=0.02
g=10
v0=10
print("The maximum height reached by the object:",(10**2)/(2*10))
def dvdt(x,y,t):
    return (-gamma*y)-g
def dxdt(x,y,t):
    return (y)

sho.rks(dxdt,dvdt,0,10,0,2)
plt.show()
##In the plot we can see that, max height reached is 5 units
##The object has minimum velocity near max height

##OUTPUT
#The maximum height reached by the object: 5.0