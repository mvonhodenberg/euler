g = open('11grid.txt', 'r')
lines = g.readlines()
for x in lines:
    x = ''.join(x.split())
print(lines)
