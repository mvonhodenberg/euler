x=[1,1]
f=0
s=0
while f==0:
    x.append(x[-1]+x[-2])
    if x[-1]>4000000:
        f=1
        x.pop()
for i in x:
    if i%2==0:
        s+=i
print(s)
