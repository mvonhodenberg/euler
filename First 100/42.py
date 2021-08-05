f=open("p042_words.txt","r")
t=f.read()
words=t.replace('"','').split(',')
count=0
triangles=[]
for i in range(1,100):
    triangles.append(int(i*(i+1)/2))
for word in words:
    score=0
    for j in range(0,len(word)):
        score+=ord(word[j].lower())-96
    if score in triangles:
        count+=1
print(count)
