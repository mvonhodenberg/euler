#easy to show through checking numbers that we only need
#to concatenate up to 200000
d=""
for i in range(1,200000):
    d+=str(i)
p=1
for k in range(1,7):
    p=p*int(d[10**k-1])
print(p)
