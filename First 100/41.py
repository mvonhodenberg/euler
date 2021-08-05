def CheckPandigital(n):
    if "0" in str(n):
        return False
    for i in range(1,len(str(n))+1):
        if str(i) not in str(n):
            return False
    return True
primes_under_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def isPrime(n):
    if n <= 100:
        return n in primes_under_100
    if n % 2 == 0 or n % 3 == 0:
        return False

    for f in range(5, int(n ** .5), 6):
        if n % f == 0 or n % (f + 2) == 0:
            return False
    return True

pandigitalprimes=[]
#note any 8 or 9-digit pandigital number has digit sum divisible by 3 and hence is not prime
for n in range(5,10000000,6):
    if isPrime(n)==True and CheckPandigital(n)==True:
        pandigitalprimes.append(n+2)
    if isPrime(n+2)==True and CheckPandigital(n+2)==True:
        pandigitalprimes.append(n+2)
print(max(pandigitalprimes))
