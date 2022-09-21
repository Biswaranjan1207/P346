#non linear equations (bisection method)
import math
def f(x):
    return x-2*math.cos(x)
def bisect(a0,b0,e):
    step=1
    print("\n\n BISECTION METHOD IMPLEMENTATION")
    condition=True
    while condition:
        c0=(a0+b0)/2
        print('Iteration-%d, c0=%0.6f and f(c0)=%0.6f' %(step,c0,f(c0)))
        if f(a0)*f(c0)<0:
            b0=c0
        else:
            a0=c0
        step=step+1
        condition=abs(f(c0))>e
    print('\n Required root is: %0.8f'%c0)
    
#input selection
a0= input('First guess:')
b0= input('Second guess:')
e= input('Tolerable error:')

#converting input to float
a0=float(a0)
b0=float(b0)
e=float(e)

if f(a0)*f(b0)>0.0:
    print("Try again with different guess!!!")
else:
    bisect(a0,b0,e)