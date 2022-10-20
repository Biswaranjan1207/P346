import math
def f(x):
    y=(x-5)*math.exp(x)+5
    return y
def d(x):
    y = (x-4)*math.exp(x)
    return y

def main(x):
    while abs(f(x))> 10**-4:
        a=f(x)/d(x)
        x=x-a
    print("The value of x in the equation:",x)
    h=6.626*10**-34
    c=3*10**8
    k=1.381*10**-23
    print("Wein's constant b:",(h*c)/(k*x))

