import math
i=100
j=100
m=0
def isPalindrome(n):
    n_str = str(n)
    for i in range(math.floor(len(n_str) / 2)):
        if n_str[i] != n_str[-(i + 1)]:
            return False
    return True
for i in range(100,1000):
    for j in range(100,1000):
        if isPalindrome(i*j)==True and i*j>m:
            m=i*j
print(m)
