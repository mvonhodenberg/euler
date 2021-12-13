import euler as e
import numpy as np
from math import factorial
from datetime import date
from collections import Counter
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
    lines = open('11grid.txt', 'r').read().split('\n')
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
    nums=open("13file.txt","r").read().split("\n")
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



