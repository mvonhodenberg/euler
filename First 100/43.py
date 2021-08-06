import itertools
substringpandigitals=[]
primes=[2,3,5,7,11,13,17]
def CheckDivisibility(s):
    for i in range(1,8):
        if int(s[i:i+3])%primes[i-1]!=0:
            return False
    return True
pandigitals=list(itertools.permutations(["0","1","2","3","4","5","6","7","8","9"]))
for item in pandigitals:
    if item[0]!="0":
        p="".join(item)
        if CheckDivisibility(p)==True:
            substringpandigitals.append(int(p))
print(sum(substringpandigitals))
