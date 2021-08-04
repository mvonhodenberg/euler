for i in range(10,100):
    for j in range(i+1,100):
        a=list(set(str(i)) & set(str(j)))
        if i%10!=0 and j%10!=0 and a!=[]:
            li=list(str(i))
            li.remove(a[0])
            lj=list(str(j))
            lj.remove(a[0])
            s=float(int(li[0])/int(lj[0]))
            if s==i/j:
                print(i,j)
