import mylibrary.newrap as nr
import math

def f(x):
    return (x-5)*math.exp(x)+5
def d(x):
    return (x-4)*math.exp(x)
def solve():
   nr.main(5)
solve()