#Presence Check

#  Created by Tiago Ferreira on 18/11/2015.
#  Copyright (c) 2015 Tiago Ferreira. All rights reserved.

import time

isEmpty = True

while isEmpty == True:
    name = input("Hello, what's your name? ")
    if name == "":
        print("Please tell me your name!")
        time.sleep(1)
    else:
        print("Hello " + name + ".")
        isEmpty = False
        break
