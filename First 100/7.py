def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True
count=0
n=2
while True:
    if count>=10001:
        print(n-1)
        break
    if isPrime(n)==True:
        count+=1
    n+=1
