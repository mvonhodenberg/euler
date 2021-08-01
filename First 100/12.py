import math
def noDivisors(n):
    c=0
    for i in range(1,math.floor(n**0.5)+1):
        if n%i==0:
            c+=1
    return c*2
f=0
i=0
while f==0:
    k=int(i*(i+1)*0.5)
    if noDivisors(k)>500:
        print(k)
        f=1
    i+=1
