#Lookup Table Check

#  Created by Tiago Ferreira on 22/11/2015.
#  Copyright (c) 2015 Tiago Ferreira. All rights reserved.


import time
import sys

valid = False
favouriteOptions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


while valid == False:
    favouriteNumber = int(input("Whats your favourite number from 0 to 9? "))
    if favouriteNumber in favouriteOptions:
        print("Valid... saving data.")
        time.sleep(0.5)
        valid = True
        sys.exit()
    else:
        print("Invalid, try again.")
