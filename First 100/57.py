#follows formula x=1+1/(1+x)
#so if we have expansion n/d, next is (n+2d)/(n+d)
numerators=[3]
denominators=[2]
count=0
for i in range(1,1000):
    numerators.append(numerators[-1]+2*denominators[-1])
    denominators.append(numerators[-2]+denominators[-1])
    if len(list(str(numerators[-1])))>len(list(str(denominators[-1]))):
        count+=1
print(count)
