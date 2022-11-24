import math
import matplotlib.pyplot as plt
import mylibrary.shooting as shoot
def dzdx(z,y,x):
    return 0.01*(y-293)

def dTdx(z,y,x):
    return (z)
x0=0.0#initial position
y0=313.0#temp at initial position
xn=10.0#total length available
dx=0.1
a=313.0
b=473.0
l=0.5#initial slope guess
h=l
y=float(shoot.couple1(dzdx,dTdx,l,y0,x0,xn,dx)-b)
while abs(y)>10**-4:
    if (y)<b:
        h=h+5.0
    else:
        h=h-5.0
    c = l + ((h-l)*(b-float(shoot.couple1(dzdx,dTdx,l,y0,x0,xn,dx))))/(float(shoot.couple1(dzdx,dTdx,h,y0,x0,xn,dx))-float(shoot.couple1(dzdx,dTdx,l,y0,x0,xn,dx)))
    y=float(shoot.couple1(dzdx,dTdx,c,y0,x0,xn,dx)-b)
#fplot.main(ff,x0,xn)
print("The slope value after interpolation:",c)
yn=373
print("The position x at which the temperature is 100 C(=373 K):",shoot.couple2(dzdx,dTdx,c,a,yn,x0,xn,dx*0.001))
plt.axhline(y = a, color = 'black')#available length initial
plt.axhline(y = b, color = 'black')#available length final
plt.xlabel("Position(x)")
plt.ylabel("Temperature(Kelvin)")
plt.show()