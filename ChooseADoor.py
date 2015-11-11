#!/usr/bin/env python

#ChooseADoor

#  Created by Tiago Ferreira on 25/09/2015.
#  Copyright (c) 2015 Tiago Ferreira. All rights reserved.

from random import randint
import time
import sys
print("Welcome mortal, to the Choose a door game...")
Score = 1
StrScore = str(Score)
Dead = False
WantsToPlay = True

positiveOptions = ["YES","yes","Yes","y","Y","Yup","yup","sim","s"]



while WantsToPlay == True:

    tutorialRequired = input("Would you like to go through the tutorial? (YES / NO): ")

    if tutorialRequired in positiveOptions:
        print("""Alright mortal, you were kidnaped and you wake up in a room.
    There are 3 doors, two of them let you continue,
    one of them gives you a painful death...
    Yeah, sorry about that...
        """)
        ready = input("Ready mortal? (YES / NO): ")
        if ready in positiveOptions:
            print("Starting game in 3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...")
            time.sleep(1)
            print("GO!")
            time.sleep(1)
        else:
            print("Goodbye mortal.")
            sys.exit()
    else:
        print("""Alright smarty pants let's see if you live to tell your story...
        """)
        ready = input("Ready mortal? (YES / NO): ")
        if ready in positiveOptions:
            print("Starting game in 3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...")
            time.sleep(1)
            print("GO!")
            time.sleep(1)
        else:
            print("Goodbye mortal.")
            sys.exit()


    while Score < 10:
        print("Three doors ahed... ")
        door = input("Pick one (1, 2, 3): ")
        doorNum = int(door)
        if door in ("123"):
            DeathDoor = randint(1,3)
            if DeathDoor == int(door):
                print("End of line, mortal.")
                StrScore = str(Score)
                if Score > 1:
                    print("You passed " + StrScore + (" doors until the endo of your miserable life..."))
                else:
                    print("You passed " + StrScore + (" door until the endo of your miserable life..."))
                Score = 1
                Dead = True
                break
            else:

                RandomNum = randint(1,3)
                if RandomNum == 1:
                    print("You're safe for now, mortal. Go on.")
                    Score = (Score + 1)
                elif RandomNum == 2:
                    print(" Beginner's luck. Let's see if you laugh next time mortal.")
                    Score = (Score + 1)
                elif RandomNum == 3:
                    print(" Keep the fireworks, they may be useful for your funeral. Go on.")
                    Score = (Score + 1)
        else:
            print("Don't try to fool me,")
            print("goodbye mortal.")
            StrScore = str(Score)
            if Score > 1:
                print("You passed " + StrScore + (" doors until the endo of your miserable life..."))
            else:
                print("You passed " + StrScore + (" door until the endo of your miserable life..."))
            Score = 0
            Dead = True
            time.sleep(1)
            sys.exit()
    if Dead:
        print("Goodbye mortal.")
    else:
        StrScore = str(Score)
        print("Congratulations mortal, you live. For now.")

    PlayAgain = input("Do you want to play again? ")

    if PlayAgain in positiveOptions:
        print("Alright, mortal.")
    else:
        print("Goodbye mortal.")
        break
