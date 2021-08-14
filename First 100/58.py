#As in p28, we can find formulae for the diagonal numbers.
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
p=3
np=2
i=3
while p/(p+np)>0.1:
    i+=2
    new=[i**2-2*i+2,i**2-3*i+3,i**2-i+1]
    np+=1
    for item in new:
        if isPrime(item)==True:
            p+=1
        else:
            np+=1
print(i)
