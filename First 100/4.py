i=100
j=100
m=0
def isPalindrome(n):
    l=list(str(n))
    if len(l)%2==1:
        x=int((len(l)-1)/2)
        l.remove(l[x])
    for i in range(0,int(len(l)/2)):
        if l[i]!=l[-(i+1)]:
            return False
    return True
for i in range(100,1000):
    for j in range(100,1000):
        if isPalindrome(i*j)==True and i*j>m:
            m=i*j
print(m)

