#String Test Mine

#  Created by Tiago Ferreira on 19/01/2016.
#  Copyright (c) 2016 Tiago Ferreira. All rights reserved.

import time
import sys

WhantsToExit = False;

print("Welcome to G00gle! (please don't confuse with Google, the search engine.)")
print("G00gle gives you information on a string you enter.")

while WhantsToExit == False:
    time.sleep(0.5)
    print()
    print("What do you want to do?")
    time.sleep(0.5)
    print()
    print("1 - Check for alphabetical characters.")
    time.sleep(0.2)
    print("2 - Check for numerical characters.")
    time.sleep(0.2)
    print("3 - Check for non-alphanumerical characters.")
    time.sleep(0.2)
    print()
    print("4 - Exit.")

    UserChoice = int(input("Answer (1, 2, 3, 4): "))

    if UserChoice == 4:
        print("Alright, see you!")
        time.sleep(0.3)
        sys.exit()
    elif UserChoice == 3:
        string = input("So, what's the string you want to use? ")
        time.sleep(0.2)
        print('"' + string + '" it is!')
        time.sleep(0.2)

        IsAplphaNum = True
        DidntFinish = True
        while DidntFinish == True:
            for letter in string:
                if letter.isalnum() == 0:
                    IsAplphaNum = False
            DidntFinish = False

        if IsAplphaNum == True:
            print("No non-alphanumerical characters here, sorry.")
            time.sleep(2)
        else:
            print("This strings has non-alphanumerical characters.")
            time.sleep(2)

    elif UserChoice == 2:
        string = input("So, what's the string you want to use? ")
        time.sleep(0.2)
        print('"' + string + '" it is!')
        time.sleep(0.2)

        IsDigit = False
        DidntFinish = True
        while DidntFinish == True:
            for letter in string:
                if letter.isdigit() == 1:
                    IsDigit = True
            DidntFinish = False

        if IsDigit == True:
            print("This string has numeric characters.")
            time.sleep(2)
        else:
            print("No numeric characters in this one, sorry.")
            time.sleep(2)

    elif UserChoice == 1:
        string = input("So, what's the string you want to use? ")
        time.sleep(0.2)
        print('"' + string + '" it is!')
        time.sleep(0.2)

        IsAlphabetical = False
        DidntFinish = True
        while DidntFinish == True:
            for letter in string:
                if letter.isalpha() == 1:
                    IsAlphabetical = True
            DidntFinish = False

        if IsAlphabetical == True:
            print("This string has alphabetical characters.")
            time.sleep(2)
        else:
            print("No alphabetical characters here, sorry.")
            time.sleep(2)
