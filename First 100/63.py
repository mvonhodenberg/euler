#To find an upper bound, note 10^n always has n+1 digits, and so we can always stop at 10.
#Now to find maximal n, note we stop at 9^n<10^(n-1), so when 1-1/n>log9 i.e n>1/(1-log9)
#i.e we need n<22
count=0
for n in range(1,22):
    for i in range(1,10):
        if 10**(n-1)<=i**n<10**n:
            count+=1
print(count)
