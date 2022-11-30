import math
import mylibrary.newrap as nr
def f(x):
    y=2.5-x*math.exp(x)
    return y
def d(x):
    y = -math.exp(x)-x*math.exp(x)
    return y
nr.main(f,d,1)

##OUTPUT
#No. of iterations in newton raphson method: 5
#The root of the equation using newton raphson method: 0.959