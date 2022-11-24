import math
import matplotlib.pyplot as plt
import mylibrary.rk4sho as sho
#2y"+(gamma)y'+2y=2cos(wt)
#gamma=0.2
#w=1.2
def dvdt(x,y,t):
    return (-0.1*y)-x + math.cos(1.2*t)
def dxdt(x,y,t):
    return (y)
sho.rks(dxdt,dvdt,2,-1,0,100)#y(0)=2 & y'(0)=-1
                            #iterating from t=0 to 100 units
plt.xlabel("Time (t)")
plt.ylabel("Position (y)")
plt.show()