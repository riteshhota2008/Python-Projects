"""Program to find the factorial values of numbers for some given number of inputs"""

import sys

def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * fact(n - 1)


num = int(input("Enter a number: "))
if (num < 0 or num >= 1000):
    print("Error; number must be positive or less than 1000")
    sys.exit()
print(num)
print(fact(num))
