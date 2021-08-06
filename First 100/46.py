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
primes=[2]
n=3
flag=0
while flag==0:
    if isPrime(n)==True:
        primes.append(n)
    else:
        goldbach=0
        for prime in primes:
            if math.sqrt((n-prime)/2).is_integer()==True:
                goldbach=1
        if goldbach==0:
            flag=1
            print(n)
    n+=2
