""""Find e to the Nth Digit
Enter a number and have the program generate e up to that many decimal places."""

import math


def CalculateE(roundVal):
    someE = round(math.e, roundVal)
    e = str(someE)
    someList = list(e)
    return someE


roundTo = input('Enter the number of digits you want after the decimal for e: ')
try:
    roundint = int(roundTo)
    print (CalculateE(roundint))
except:
    print ("You did not enter an integer")
