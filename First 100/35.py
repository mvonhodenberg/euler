def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True
def allPrime(l):
    for i in range(0,len(l)):
        if isPrime(l[i])==False:
            return False
    return True
def ReturnRotations(n):
    l=[]
    z=list(str(n))
    if len(z)==1:
        return [n]
    for i in range(0,len(z)):
        x=z.pop()
        a=""
        z.insert(0,x)
        for item in z:
            a+=item
        l.append(int(a))
    return l

circularprimes=[2]
for i in range(3,1000000,2):
    if isPrime(i)==True:
        if allPrime(ReturnRotations(i))==True:
            circularprimes.append(i)
print(len(circularprimes))
