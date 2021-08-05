import math

#for a perimeter of p, with  a triple {a,b,c} we know a,b<c<a+b
#so p<2a+2b -> a>p/2-b and p>2a+b so a<1/2(p+b)
maxp=0
maxn=0
for p in range(5,1000):
    pn=0
    plist=[]
    for b in range(1,math.ceil(p/2)):
        for a in range(math.floor(p/2)-b,math.ceil((p+b)/2)):
            if a**2+b**2==(p-a-b)**2 and a not in plist and b not in plist:
                pn+=1
                plist.append(a)
    if pn>maxn:
        maxn=pn
        maxp=p
print(maxp)
