#number of paths on nxn is equiv to arranging n D's along with 2n R's: so is 2n choose n.
def f(n):
    x=1
    for i in range(1,n+1):
        x=x*i
    return x
print(int(f(40)/(f(20)**2)))
