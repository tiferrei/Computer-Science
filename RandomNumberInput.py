import random
import sys
import time

NumberOne = random.randint(1,5000)
NumberTwo = random.randint(1,5000)
Again = True

while Again == True:

    Operation = input("Which operation do you want to use? (+, -, :, x)")

    if Operation == "+":
        total = (NumberOne + NumberTwo)
        print("Your random number is: " + str(total))
    elif Operation == "-":
        total = (NumberOne - NumberTwo)
        print("Your random number is: " + str(total))
    elif Operation == ":":
        total = (NumberOne / NumberTwo)
        print("Your random number is: " + str(total))
    elif Operation == "x":
        total = (NumberOne * NumberTwo)
        print("Your random number is: " + str(total))

    AgainYN = input("Do you want to do another operation? (YES, NO)")
    if AgainYN == "YES":
        time.sleep(1)
    else:
        break
        sys.exit()
