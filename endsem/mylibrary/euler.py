def f(x,y):
    return (x)
def euler(x0,y,h,x):
    while x0<x:
        y=y+h*f(x0,y)
        x0+=h
    print("Solution at x=",x,"is:",y)
euler(0,0,0.0001,0.1)