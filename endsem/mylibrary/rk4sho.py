import matplotlib.pyplot as plt
import math
def rks(dxdt,dvdt,x,v,t,tn):
    dt=0.01
    V=[]
    T=[]
    X=[]
    while t<tn:
        k1x= dt*dxdt(x,v,t)
        k1v=dt*dvdt(x,v,t)
        k2x=dt*dxdt(x+k1x/2,(v+k1v/2),(t+dt/2))
        k2v=dt*dvdt((x+k1x/2),v+k1v/2,(t+dt/2))
        k3x=dt*dxdt(x+k2x/2,(v+k2v/2),(t+dt/2))
        k3v=dt*dvdt((x+k2x/2),v+k2v/2,(t+dt/2))
        k4x=dt*dxdt(x+k3x,(v+k3v),(t+dt))
        k4v=dt*dvdt((x+k3x),v+k3v,(t+dt))
        kx=(k1x+2*k2x+2*k3x+k4x)/6
        kv=(k1v+2*k2v+2*k3v+k4v)/6
        x=x+kx
        X.append(x)
        v=v+kv
        V.append(v)
        t+=dt
        T.append(t)
    plt.plot(X,V)
    plt.xlabel("Height")
    plt.ylabel("Velocity")