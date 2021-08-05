TruncatablePrimes=[]
def isPrime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def TruncateListPrime(n):
    l=[n]
    for i in range(1,len(str(n))):
        l.append(int(str(n)[i:]))
        l.append(int(str(n)[:i]))
    for num in l:
        if isPrime(num)==False:
            return False
    return True
i=10
while len(TruncatablePrimes)<11: #we are given there are only 11 truncatable primes
    if isPrime(i)==True:
         if TruncateListPrime(i)==True:
             TruncatablePrimes.append(i)
    i+=1
print(sum(TruncatablePrimes))
