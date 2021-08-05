def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True
'''
f(0)=b=p
f(1)=1+a+p=q

so a=q-p-1
'''
maxc=0
a=0
b=0
for p in range(1,1001,2): #brute force check over all p and thus over a and b, with step size of 2 for only primes
    for q in range(1,1001,2):
        if isPrime(p)==True and isPrime(q)==True and isPrime(2-p+2*q)==True: #checks f(0),f(1),f(2) to reduce iterations
            c=0
            for n in range(0,1000):
                if isPrime(n**2+n*(-p+q-1)+p)==True:
                    c+=1
                else:
                    if c>maxc: #if no. consecutive primes new high
                        maxc=c
                        a=q-p-1
                        b=p
                    break
print(a*b)
