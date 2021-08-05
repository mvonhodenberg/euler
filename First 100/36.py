import math
def isPalindrome(n):
    n_str = str(n)
    for i in range(math.floor(len(n_str) / 2)):
        if n_str[i] != n_str[-(i + 1)]:
            return False
    return True

nums=[]
for i in range(1,1000000,2): #only odd as no leading 0s in binary
    if isPalindrome(i)==True and isPalindrome(bin(i)[2:])==True:
        nums.append(i)
print(sum(nums))
