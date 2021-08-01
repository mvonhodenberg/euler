def d(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    return s
a=[]
s=0
for i in range(1,10000):
    if d(d(i))==i and d(i)!=i:
        a.append(i)
for j in a:
    s+=j
print(s)
print(a)
