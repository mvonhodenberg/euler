import math
def iterate_p55(n):
    l=list(str(n))
    l.reverse()
    r=int("".join(l))
    return n+r
def isPalindrome(n):
    n_str = str(n)
    for i in range(math.floor(len(n_str) / 2)):
        if n_str[i] != n_str[-(i + 1)]:
            return False
    return True
def isLychrel(n):
    current=iterate_p55(n)
    count=0
    while count<50:
        if isPalindrome(current)==True:
            return False
        current=iterate_p55(current)
        count+=1
    return True
lychrel=[]
for n in range(1,10000):
    if isLychrel(n)==True:
        lychrel.append(n)
print(len(lychrel))
