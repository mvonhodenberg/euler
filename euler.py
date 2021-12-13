import math
from math import sqrt


def fib(n):
    return int(round(((1 + sqrt(5))/2)**n / sqrt(5)))

def isPalindrome(n):
    return bool(str(n)==str(n)[::-1])