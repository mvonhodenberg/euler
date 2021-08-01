import math
def isAbundant(n):
    l=[1]
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n%i==0:
            l.append(i)
            if int(n/i)!=i:
                l.append(int(n/i))
    s=0
    for i in l:
        s+=i
    if s<=n:
        return False
    return True
a=[]
for i in range(1,10000):
    if isAbundant(i)==True:
        a.append(i)
print(a)
