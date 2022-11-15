import mylibrary.integration as intg
import math
def f1(x):
    return (math.sin(x))**2
print("The value of the integral by Monte Carlo method:",intg.moncar(f1,-1,1,1000))