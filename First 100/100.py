#For b blues and t total, we want 2b(b-1)=t(t-1).
#So since b/t>(b-1)/(t-1), we have b>t/sqrt2 and b<1+(t-1)/sqrt2
import math
for t in range(1,10**8):
    for b in range(math.floor(t/(2**0.5)),1+math.ceil((t-1)/(2**0.5))):
        if t*(t-1)==2*b*(b-1):
            print(b,t)
