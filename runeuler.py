import first100
n=int(input('Enter the number of the question you would like to solve: '))
print('Output:')
try:
    eval(f'print(first100.q{n}'+'())')
except:
    print('This problem has not been solved yet, sorry!')