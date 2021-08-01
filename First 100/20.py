n=1
s=0
for i in range(1,101):
    n=n*i
l=list(str(n))
for x in l:
    s+= int(x)
print(s)
