import math
primes_under_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def isPrime(n):
    if n <= 100:
        return n in primes_under_100
    if n % 2 == 0 or n % 3 == 0:
        return False

    for f in range(5, math.ceil(n ** .5), 6):
        if n % f == 0 or n % (f + 2) == 0:
            return False
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
i=2
while True:
    l=[i,i+1,i+2,i+3]
    if set([GetNoDistinctPrimeFactors(x) for x in l])=={4}:
        print(i)
        break
    i+=1
