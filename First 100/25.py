f=[1,1]
i=2
while len(str(f[i-1]))<1000:
    f.append(f[i-1]+f[i-2])
    i+=1
print(i)
