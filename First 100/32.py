#first note our only options for no.digits are 2,3,4 or 1,4,4
a=[]
#2,3,4
for i in range(10,100):
    for j in range(100,1000):
        if "0" not in list(str(i)) and "0" not in list(str(j)) and "0" not in list(str(i*j)):
            if len(set(str(i)))==len(list(str(i))) and len(set(str(j)))==len(list(str(j))) and len(set(str(i*j)))==len(list(str(i*j))):
                if [x for x in list(str(i)) if x in list(str(j))]==[] and i*j<10000:#checks if they share a digit and if product is 4 digits
                    if [x for x in list(str(i*j)) if x in list(str(j)) or x in list(str(i))]==[] and i*j not in a:
                        a.append(i*j)
#1,4,4
for i in range(1,10):
    for j in range(1000,10000):
        if "0" not in list(str(i)) and "0" not in list(str(j)) and "0" not in list(str(i*j)):
            if len(set(str(i)))==len(list(str(i))) and len(set(str(j)))==len(list(str(j))) and len(set(str(i*j)))==len(list(str(i*j))):
                if [x for x in list(str(i)) if x in list(str(j))]==[] and i*j<10000:#checks if they share a digit and if product is 4 digits
                    if [x for x in list(str(i*j)) if x in list(str(j)) or x in list(str(i))]==[] and i*j not in a:
                        a.append(i*j)
print(sum(a))    
