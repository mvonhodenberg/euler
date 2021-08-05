def ConcatenateProduct(n):
    s=""
    i=1
    while len(s)<9:
        s+=str(i*n)
        i+=1
    if len(s)==9:
        return s
    else:
        return ""
def CheckPandigital(s):
    if len(s)==0:
        return False
    if "0" not in list(s) and len(set(s))==len(list(s)):
        return True
products=[]
for i in range(1,10000):
    if CheckPandigital(ConcatenateProduct(i))==True:
        products.append(int(ConcatenateProduct(i)))
print(max(products))
