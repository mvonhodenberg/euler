f=open("p022_names.txt","r")
t=f.read()
names=t.replace('"','').split(',')
s=sorted(names)
score=0
for i in range(0,len(s)):
    x=0
    m=s[i]
    for j in range(0,len(m)):
        x+=ord(m[j].lower())-96
    score+=(i+1)*x
print(score)
