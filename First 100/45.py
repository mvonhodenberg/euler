triangle=[]
pentagon=[]
hexagon=[]
def GenerateNums(n):
    for i in range(1,n):
        hexagon.append(i*(2*i-1))
    j=1
    while int(j*(j+1)/2)<hexagon[-1]:
        triangle.append(int(j*(j+1)/2))
        j+=1
    k=1
    while int(k*(3*k-1)/2)<hexagon[-1]:
        pentagon.append(int(k*(3*k-1)/2))
        k+=1
n=100000
GenerateNums(n)
for i in range(0,n-1):
    if hexagon[i]>40755 and (hexagon[i] in triangle) and (hexagon[i] in pentagon):
        print(hexagon[i])
