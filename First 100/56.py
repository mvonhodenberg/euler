maxsum=0
def digitsum(n):
    x=0
    for digit in list(str(n)):
        x+=int(digit)
    return x
for a in range(100):
    for b in range(100):
        if digitsum(a**b)>maxsum:
            maxsum=digitsum(a**b)
print(maxsum)
