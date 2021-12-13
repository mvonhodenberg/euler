i=1
while True:
    f=0
    for j in range(1,7):
        if sorted(str(i))!=sorted(str(i*j)):
            f=1
            break
    if f==0:
        print(i)
        break
    i+=1
