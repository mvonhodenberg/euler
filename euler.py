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