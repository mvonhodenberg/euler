def f(n):
    if n==1:
        return 1
    else:
        return n*f(n-1)
#2683715490
print(1000000-2*f(9)-6*f(8)-6*f(7)-2*f(6)-5*f(5)-f(4)-2*f(3))
0,4,9 left
