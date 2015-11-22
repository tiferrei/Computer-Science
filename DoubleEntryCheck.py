#Double Entry Check

#  Created by Tiago Ferreira on 22/11/2015.
#  Copyright (c) 2015 Tiago Ferreira. All rights reserved.

import sys
import time

passwordMatches = False

while passwordMatches == False:
    password = input("New password: ")
    CheckPassword = input("Re-enter new password: ")

    if password == CheckPassword:
        print("Password changed.")
        time.sleep(0.5)
        passwordMatches = True
        sys.exit()
    else:
        print("Passwords don't match, please try again.")
        time.sleep(0.5)
        
