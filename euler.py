from math import sqrt,ceil,floor

def fib(n):
    return int(round(((1 + sqrt(5))/2)**n / sqrt(5)))

def isPalindrome(n):
    return bool(str(n)==str(n)[::-1])

def isPrime(n):
    primes_under_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if n <= 100:
        return n in primes_under_100
    if n % 2 == 0 or n % 3 == 0:
        return False
    for f in range(5, ceil(n ** .5)+1, 6):
        if n % f == 0 or n % (f + 2) == 0:
            return False
    return True

def primeno(n):
    a=0
    i=0
    while a<n:
        i+=1
        if isPrime(i):
            a+=1
    return i

def noDivisors(n):
    c=0
    for i in range(1,floor(n**0.5)+1):
        if n%i==0:
            c+=1
    return c*2

def CollatzLength(n):
    i=n
    c=1
    while i!=1:
        if i%2==0:
            i=int(i/2)
        else:
            i=3*i+1
        c+=1
    return c

def d(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    return s

def allPrime(l):
    for x in l:
        if isPrime(x)==False:
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

def TruncateListPrime(n):
    l=[n]
    for i in range(1,len(str(n))):
        l.append(int(str(n)[i:]))
        l.append(int(str(n)[:i]))
    for num in l:
        if isPrime(num)==False:
            return False
    return True

def ConcatenateProduct(n):
    s=""
    i=1
    while len(s)<9:
        s+=str(i*n)
        i+=1
    if len(s)==9:
        return s
    else:
        return ""

def CheckPandigital(s):
    s=str(s)
    if len(s)==0:
        return False
    if "0" not in list(s) and len(set(s))==len(list(s)):
        return True

def GetNoDistinctPrimeFactors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return len(set(factors))

def digitsum(n):
    return sum([int(x) for x in list(str(n))])