# since 9!=362880, we cannot have 8 digit numbers or larger.
# to optimise further, we can only have odd numbers if they contain a 1, since all other factorials are even
#for any no >362880 we must have a 9 in the number, as 8*8!<9!
def factorial(n):
    if n==1 or n==0:
        return 1
    x=1
    for i in range(2,n+1):
        x=x*i
    return(x)
l=[]
for i in range(3,362880):
    z=list(str(i))
    if i%2==0 or "1" in z or "0" in z:
        s=0
        for j in z:
            s+=factorial(int(j))
        if s==i:
            print(s)
for i in range(362880,9999999):
    z=list(str(i))
    if "9" in z and (i%2==0 or "1" in z or "0" in z):
        s=0
        for j in z:
            s+=factorial(int(j))
        if s==i:
            print(s)
