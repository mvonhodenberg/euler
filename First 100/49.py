import math
import itertools
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
ans=set()
for i in range(1000,10000):
    if isPrime(i)==True and i not in ans:
        perms=list(itertools.permutations(list(str(i))))
        perms2=[]
        for item in perms:
            perms2.append(int("".join(item)))
        y=list(set([x for x in perms2 if isPrime(x)==True and len(str(x))==4]))
        y.sort()
        for item in y:
            ans.add(item)
            for i in range(0,len(y)-1):
                if item+(item-y[i]) in y and item!=y[i]:
                    print(y[i],item,item+(item-y[i]))
