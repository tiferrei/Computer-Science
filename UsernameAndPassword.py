#Username And Password

#  Created by Tiago Ferreira on 25/11/2015.
#  Copyright (c) 2015 Tiago Ferreira. All rights reserved.

import time
import sys

upercaseOptions = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                   "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numberOptions = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

specialCharOptions = ["!","@", "[", "]", "#", "€", "", "£", "$", "%", "^", "&",
                      "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "]", "~",
                      "#", ":", ";", "'", "/", "|"]


passwordIsntValid = True
validLenght = False
validNumber = False
validSpecialChar = False
validUperCase = False

username = input("Username: ")

while passwordIsntValid == True:

    password = input("Password: ")

    if len(password) > 7:
        validLenght = True

    for character in password:
        if character in upercaseOptions:
            validUperCase = True
        if character in numberOptions:
            validNumber = True
        if character in specialCharOptions:
            validSpecialChar = True


    if validLenght == True and validSpecialChar == True and validNumber == True and validUperCase == True:
        print("Your password is valid.")

        checkPasswordIsntValid = True

        while checkPasswordIsntValid == True:

            checkPassword = input("Please retype your password: ")

            if password == checkPassword:
                print("Passwords match.")
                time.sleep(0.5)
                print("Password saved.")
                print("Password: " + username)
                print("Password: " + password)
                sys.exit()
            else:
                print("Passwords don't match, please try again.")
    else:
        print("""Your password must have at least 8 characters, 1 number, 1 upper
        case letter and a special character. Please try again.""")
