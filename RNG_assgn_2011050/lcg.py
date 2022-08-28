import matplotlib.pyplot as plt
def lcg():
    x=10
    n=1000
    a=1103515245
    c=12345
    m=32768
    xlist=[]
    ylist=[]
    for i in range (0,n):
        x=(a*x+c)%m
        xlist.append(x/m)
        ylist.append(i+1)
    plt.plot(ylist,xlist,'.')
    plt.show()
lcg()