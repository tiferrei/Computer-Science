#Range Check

#  Created by Tiago Ferreira on 18/11/2015.
#  Copyright (c) 2015 Tiago Ferreira. All rights reserved.

import time

WrongRange = True

while WrongRange == True:
    Age = int(input("Hi, what's your age? "))
    if Age > 13 and Age < 19:
        print("Your age is valid, welcome.")
        break
    else:
        print("Your age is invalid, please try again.")
        time.sleep(1)
