#numbers on upper right diagonal are all odd squares, (i^2)
#and lower left are numbers halfway between two consecutive odd squares (i^2-2i+2)
#other diags are numbers 1/4 or 3/4 of the way between (i^2-3i+3),(i^2-i+1)
n=1
for i in range(3,1002,2):
    n+=i**2+(i**2-2*i+2)+(i**2-3*i+3)+(i**2-i+1)
print(n)
