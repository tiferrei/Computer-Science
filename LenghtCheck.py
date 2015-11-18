#Length Check

#  Created by Tiago Ferreira on 18/11/2015.
#  Copyright (c) 2015 Tiago Ferreira. All rights reserved.

import time

password = input("New password: ")
tooShort = True

while tooShort == True:

    if len(password) < 8:
        print("You're password is too short.")
    else:
        print("Password saved.")
        tooShort = False
    time.sleep(0.5)
