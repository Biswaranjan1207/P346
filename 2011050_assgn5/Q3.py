import mylibrary.integration as intg
import math
def f2(x):
    return x**2
def f3(x):
    return x**3
def solve():
    x1=intg.moncar(f2,0,2,1000)
    x2=intg.moncar(f3,0,2,1000)
    cm=x2/x1
    print("The centre of mass of the beam lies in:",cm,"m")
solve()