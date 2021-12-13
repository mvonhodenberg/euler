import euler as e

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

def q4():
    m=0
    for i in range(100,1000):
        for j in range(100,1000):
            if e.isPalindrome(i*j)==True and i*j>m:
                m=i*j
    return m

def q5():
    return (2**4)*(3**2)*5*7*11*13*17*19

def q6():
    return 5050**2-((10100*201)/6)

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
print(q9())