import euler as e
import numpy as np
from math import factorial,floor,ceil,sqrt
from datetime import date
from collections import Counter
from itertools import permutations
#I have put many algorithms in euler.py which form the bulk of some questions.

def q1():
    return sum([i if (i%3==0 or i%5==0) else 0 for i in range(1,1000)])

def q2():
    s=0
    n=0
    while e.fib(n)<=4000000:
        if e.fib(n)%2==0:
            s+=e.fib(n)
        n+=1
    return s

def q3():
    #using a recursive method
    n = 600851475143
    i = 2
    while i**2 < n:
        while n%i == 0:
            n=n/i
        i+=1
    return n

def q4():
    m=0
    for i in range(100,1000):
        for j in range(100,1000):
            if e.isPalindrome(i*j)==True and i*j>m:
                m=i*j
    return m

def q5():
    #using prime factiorisation
    return (2**4)*(3**2)*5*7*11*13*17*19

def q6():
    #simply using sum formula
    return 5050**2-((10100*201)/6)

def q7():
    return e.primeno(10001)
def q8():
    n=7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    m=0
    for i in range(0,1000):
        l = [int(x) for x in list(str(n)[i:i+13])]
        a=1
        for i in l:
            a*=i
        if a>m:
            m=a
    return m

def q9():
    for i in range(0,500):
        for j in range(0,500):
            if i**2+j**2==(1000-i-j)**2:
                return (i*j*(1000-i-j))

def q10():
    s=0
    for i in range(2,2000000):
        if e.isPrime(i)==True:
            s+=i
    return s

def q11():
    lines = open('files/p011_grid.txt', 'r').read().split('\n')
    grid=[]
    for line in lines:
        grid.append([int(x) for x in line.split(' ')])
    grid=np.array(grid)
    maxprod=0
    for i in range(20):
        for j in range(17):
            if np.prod(grid[i][j:j+4])>maxprod:
                maxprod=np.prod(grid[i][j:j+4])
    for i in range(17):
        for j in range(20):
            if grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]>maxprod:
                maxprod=grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
    for i in range(17):
        for j in range(17):
            diag1=grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
            diag2=grid[19-i][j]*grid[18-i][j+1]*grid[17-i][j+2]*grid[16-i][j+3]
            if diag1>maxprod:
                maxprod=diag1
            if diag2>maxprod:
                maxprod=diag2
    return maxprod

def q12():
    i=0
    while True:
        k=int(i*(i+1)*0.5)
        if e.noDivisors(k)>500:
            return k
        i+=1

def q13():
    nums=open("files/p013_file.txt","r").read().split("\n")
    return str(sum([int(x) for x in nums]))[:10]

def q14():
    m=0
    n=0
    for i in range(2,1000000):
        if e.CollatzLength(i)>m:
            m=e.CollatzLength(i)
            n=i
    return n

def q15():
    #number of paths on nxn is equiv to arranging n D's along with 2n R's: so is 2n choose n.
    return int(factorial(40)/(factorial(20)**2))

def q16():
    return sum([int(x) for x in list(str(2**1000))])

def q17():
    n1=(0,3,3,5,4,4,3,5,5,4)    # 1 to 9
    n10=(0,3,6,6,5,5,5,7,6,6)   # 10 to 90
    n11=(0,6,6,8,8,7,7,9,8,8)   # 11 to 19
    n=(7,10,11) # hundred, hundred and, one thousand

    n1to99x10 = (sum(n1)*9 + n10[1] + sum(n11) + sum(n10[2:])*10)*10 # from 1 to 99 all
    n100to900all = n[0]*9 + n[1]*99*9 + sum(n1)*100 # from 100 to 900
    
    letters = n1to99x10 + n100to900all + n[2]
    return letters

def q19():
    counter = Counter()

    for year in range(1901, 2001):
        for month in range(1, 13):
            day = date(year, month, 1)
            counter[day.weekday()] += 1

    return counter[6]

def q20():
    return sum([int(x) for x in list(str(factorial(100)))])

def q21():
    a=[]
    s=0
    for i in range(1,10000):
        if e.d(e.d(i))==i and e.d(i)!=i:
            a.append(i)
    for j in a:
        s+=j
    return s

def q22():
    f=open("files/p022_names.txt","r").read()
    names=sorted(f.replace('"','').split(','))
    score=0
    for i in range(0,len(names)):
        x=0
        m=names[i]
        for j in range(0,len(m)):
            x+=ord(m[j].lower())-96
        score+=(i+1)*x
    return score

def q24():
    #can be found by simple process of elimination
    return 2783915460

def q25():
    i=1
    while len(str(e.fib(i)))<1000:
        i+=1
    return i

def q27():
    maxc=0
    a=0
    b=0
    for p in range(1,1001,2): #brute force check over all p and thus over a and b, with step size of 2 for only primes
        for q in range(1,1001,2):
            if e.isPrime(p) and e.isPrime(q) and e.isPrime(2-p+2*q): #checks f(0),f(1),f(2) to reduce iterations
                c=0
                for n in range(0,1000):
                    if e.isPrime(n**2+n*(-p+q-1)+p)==True:
                        c+=1
                    else:
                        if c>maxc: #if no. consecutive primes new high
                            maxc=c
                            a=q-p-1
                            b=p
                        break
    return a*b

def q28():
    #numbers on upper right diagonal are all odd squares, (i^2)
    #and lower left are numbers halfway between two consecutive odd squares (i^2-2i+2)
    #other diags are numbers 1/4 or 3/4 of the way between (i^2-3i+3),(i^2-i+1)
    n=1
    for i in range(3,1002,2):
        n+=i**2+(i**2-2*i+2)+(i**2-3*i+3)+(i**2-i+1)
    return n

def q30():
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
    return sum(a)

def q32():
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
    return sum(a)

def q33():
    for i in range(10,100):
        for j in range(i+1,100):
            a=list(set(str(i)) & set(str(j)))
            if i%10!=0 and j%10!=0 and a!=[]:
                li=list(str(i))
                li.remove(a[0])
                lj=list(str(j))
                lj.remove(a[0])
                s=float(int(li[0])/int(lj[0]))
                if s==i/j:
                    pass
                    #printing this gives 16/64, 19/95, 26/65, 49/98. Simplifies down to 1/100.
    return 100

def q34():
    # since 9!=362880, we cannot have 8 digit numbers or larger.
    # to optimise further, we can only have odd numbers if they contain a 1, since all other factorials are even
    #for any n >362880 we must have a 9 in the number, as 8*8!<9!
    #it turns out there are no solns for n >362880, removed for runtime speed
    total=0
    for i in range(3,362880):
        z=list(str(i))
        if i%2==0 or "1" in z or "0" in z:
            s=0
            for j in z:
                s+=factorial(int(j))
            if s==i:
                total+=s
    return total

def q35():
    circularprimes=[2]
    for i in range(3,1000000,2):
        if e.isPrime(i)==True:
            if e.allPrime(e.ReturnRotations(i))==True:
                circularprimes.append(i)
    return len(circularprimes)

def q36():
    sum=0
    for i in range(1,1000000,2): #only odd as no leading 0s in binary
        if e.isPalindrome(i)==True and e.isPalindrome(bin(i)[2:])==True:
            sum+=i
    return sum

def q37():
    TruncatablePrimes=[]
    i=10
    while len(TruncatablePrimes)<11: #we are given there are only 11 truncatable primes
        if e.isPrime(i)==True:
            if e.TruncateListPrime(i)==True:
                TruncatablePrimes.append(i)
        i+=1
    return sum(TruncatablePrimes)

def q38():   
    products=[]
    for i in range(1,10000):
        if e.CheckPandigital(e.ConcatenateProduct(i))==True:
            products.append(int(e.ConcatenateProduct(i)))
    return max(products)

def q39():
    #for a perimeter of p, with  a triple {a,b,c} we know a,b<c<a+b
    #so p<2a+2b -> a>p/2-b and p>2a+b so a<1/2(p+b)
    maxp=0
    maxn=0
    for p in range(5,1000):
        pn=0
        plist=[]
        for b in range(1,ceil(p/2)):
            for a in range(floor(p/2)-b,ceil((p+b)/2)):
                if a**2+b**2==(p-a-b)**2 and a not in plist and b not in plist:
                    pn+=1
                    plist.append(a)
        if pn>maxn:
            maxn=pn
            maxp=p
    return maxp

def q40():
    #easy to show through checking numbers that we only need to concatenate up to 200000
    d=""
    for i in range(1,200000):
        d+=str(i)
    p=1
    for k in range(1,7):
        p=p*int(d[10**k-1])
    return p

def q41():
    max=0
    return 7652413
    #note any 8 or 9-digit pandigital number has digit sum divisible by 3 and hence is not prime
    ''' need to improve performance of this
    for n in range(5,10000000,6):
        if e.isPrime(n)==True and e.CheckPandigital(n)==True:
            max=n+2
        if e.isPrime(n+2)==True and e.CheckPandigital(n+2)==True:
            max=n+2
    return max
    '''

def q42():
    f=open("files/p042_words.txt","r")
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
    return count


def CheckDivisibility(s):
    primes=[2,3,5,7,11,13,17]
    for i in range(1,8):
        if int(s[i:i+3])%primes[i-1]!=0:
            return False
    return True
def q43():
    sum=0
    pandigitals=list(permutations(["0","1","2","3","4","5","6","7","8","9"]))
    for item in pandigitals:
        if item[0]!="0":
            p="".join(item)
            if CheckDivisibility(p)==True:
                sum+=int(p)
    return sum

def q46():
    primes=[2]
    n=3
    while True:
        if e.isPrime(n)==True:
            primes.append(n)
        else:
            goldbach=0
            for prime in primes:
                if sqrt((n-prime)/2).is_integer()==True:
                    goldbach=1
            if goldbach==0:
                return n
        n+=2

def q47():
    i=2
    while True:
        l=[i,i+1,i+2,i+3]
        if set([e.GetNoDistinctPrimeFactors(x) for x in l])=={4}:
            return i
        i+=1

def q48():
    n=0
    for i in range(1,1001):
        n+=i**i
    return str(n)[-10:]

def q49():
    ans=set()
    for i in range(1000,10000):
        if e.isPrime(i)==True and i not in ans:
            perms=list(permutations(list(str(i))))
            perms2=[]
            for item in perms:
                perms2.append(int("".join(item)))
            y=list(set([x for x in perms2 if e.isPrime(x)==True and len(str(x))==4]))
            y.sort()
            for item in y:
                ans.add(item)
                for i in range(0,len(y)-1):
                    if item+(item-y[i]) in y and item>y[i] and y[i]!=1487:
                        return str(y[i])+str(item)+str(item+(item-y[i]))

def q52():
    i=1
    while True:
        f=0
        for j in range(1,7):
            if sorted(str(i))!=sorted(str(i*j)):
                f=1
                break
        if f==0:
            return i
        i+=1

def iterate_p55(n):
    l=list(str(n))
    l.reverse()
    r=int("".join(l))
    return n+r
def isLychrel(n):
    current=iterate_p55(n)
    count=0
    while count<50:
        if e.isPalindrome(current)==True:
            return False
        current=iterate_p55(current)
        count+=1
    return True
def q55():
    lychrel=[]
    for n in range(1,10000):
        if isLychrel(n)==True:
            lychrel.append(n)
    return len(lychrel)

def q56():
    maxsum=0
    for a in range(100):
        for b in range(100):
            if e.digitsum(a**b)>maxsum:
                maxsum=e.digitsum(a**b)
    return maxsum

def q57():
    #follows formula x=1+1/(1+x)
    #so if we have expansion n/d, next is (n+2d)/(n+d)
    numerators=[3]
    denominators=[2]
    count=0
    for i in range(1,1000):
        numerators.append(numerators[-1]+2*denominators[-1])
        denominators.append(numerators[-2]+denominators[-1])
        if len(list(str(numerators[-1])))>len(list(str(denominators[-1]))):
            count+=1
    return count

def q58():
    #As in p28, we can find formulae for the diagonal numbers.
    p=3
    np=2
    i=3
    while p/(p+np)>0.1:
        i+=2
        new=[i**2-2*i+2,i**2-3*i+3,i**2-i+1]
        np+=1
        for item in new:
            if e.isPrime(item)==True:
                p+=1
            else:
                np+=1
    return i

def q63():
    #To find an upper bound, note 10^n always has n+1 digits, and so we can always stop at 10.
    #Now to find maximal n, note we stop at 9^n<10^(n-1), so when 1-1/n>log9 i.e n>1/(1-log9)
    #i.e we need n<22
    count=0
    for n in range(1,22):
        for i in range(1,10):
            if 10**(n-1)<=i**n<10**n:
                count+=1
    return count