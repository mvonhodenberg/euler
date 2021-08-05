#if our number has n digits, then the maximum value of the sum of the fifth powers of its digits is n(9^5).
#So if we have more than n digits where 10^(n-1)>n(9^5), we can't have
#the number being equal to the sum of 5th powers of it's digits, as it will always be greater.
#Plotting 10^(x-1)-9^5(x), this first happens when we have 7 digits. So only need to search up to 999999.
a=[]
for i in range(2,1000000):
    l=list(str(i))
    s=0
    for x in l:
        s+=int(x)**5
    if s==i:
        a.append(i)
print(sum(a))
