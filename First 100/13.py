f=open("13file.txt","r")
nums=f.read().split("\n")
s=0
for i in nums:
    s+=int(i)
print(s)
