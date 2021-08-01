def CollatzLength(n):
    i=n
    c=1
    while i!=1:
        if i%2==0:
            i=int(i/2)
        else:
            i=3*i+1
        c+=1
    return c
print(CollatzLength(13))
m=0
n=0
for i in range(2,1000000):
    if CollatzLength(i)>m:
        m=CollatzLength(i)
        n=i
print(n)
