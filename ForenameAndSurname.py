#Forename and Surname

#  Created by Tiago Ferreira on 07/12/2015.
#  Copyright (c) 2015 Tiago Ferreira. All rights reserved.

import sys
import time
import os



letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S"
            "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UserIsLying = True

forenameValid = False
surnameValid = False

while UserIsLying == True:

    forename = input("What's your forename? ")
    time.sleep(0.5)

    while 1 == 1:
        if forename == "":
            print("I need your forename!")
            time.sleep(0.5)
            forename = input("What's your forename? ")
        else:
            print("Not empty: OK")
            break

    
