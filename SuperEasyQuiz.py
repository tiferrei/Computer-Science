#Super Easy Quiz

#  Created by Tiago Ferreira on 22/11/2015.
#  Copyright (c) 2015 Tiago Ferreira. All rights reserved.

import sys
import time
import os

positiveOptions = ["YES","yes","Yes","y","Y","Yup","yup","sim","s"]
combinedOptions = ["A", "a", "1", 1, "B", "b", "2", 2, "C", "c", "3", 3]
firstOptions = ["A", "a", "1", 1]
secondOptions = ["B", "b", "2", 2]
thirdOptions = ["C", "c", "3", 3]
wasChicky = True
Score = 0

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

while wasChicky == True:
    print("Welcome! To the most easy quiz in the world!")
    time.sleep(0.5)
    isReady = input("Ready?")
    time.sleep(0.3)
    if isReady in positiveOptions or isReady == "":
        print("Starting game in 3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("GO!")
        time.sleep(1)
    else:
        print("Goodbye.")
        sys.exit()

    print("First question:")
    print("2 + 2 = ")
    print("A) 0")
    print("B) 2")
    print("C) 4")
    time.sleep(0.5)
    firstanswer = input("Answer: ")
    if firstanswer in combinedOptions:
        if firstanswer in thirdOptions:
            print("Well done! Here, take a cookie.")
            Score = Score + 1
            time.sleep(0.5)
        else:
            print("And a darwin award for you!")
            time.sleep(0.5)
    else:
        print("Don't try to fool me!")
        print("Restarting...")
        time.sleep(0.5)
        restart_program()

    print("Second question:")
    print("4 + 4 = ")
    print("A) 2")
    print("B) 8")
    print("C) 4")
    time.sleep(0.5)
    firstanswer = input("Answer: ")
    if firstanswer in combinedOptions:
        if firstanswer in secondOptions:
            print("WOW! Here, take another cookie!")
            Score = Score + 1
            time.sleep(0.5)
        else:
            print("And another darwin award for you!")
            time.sleep(0.5)
    else:
        print("Don't try to fool me!")
        print("Restarting...")
        time.sleep(0.5)
        restart_program()

    print("Third question:")
    print("8 + 8 = ")
    print("A) 16")
    print("B) 4")
    print("C) 8")
    time.sleep(0.5)
    firstanswer = input("Answer: ")
    if firstanswer in combinedOptions:
        if firstanswer in firstOptions:
            print("WOW! Here, take a cookie!")
            Score = Score + 1
            time.sleep(0.5)
        else:
            print("You know, that was quite easy. -_-")
            time.sleep(0.5)
    else:
        print("Don't try to fool me!")
        print("Restarting...")
        time.sleep(0.5)
        restart_program()

    print("Fourth question:")
    print("16 + 16 = ")
    print("A) 16")
    print("B) 32")
    print("C) 8")
    time.sleep(0.5)
    firstanswer = input("Answer: ")
    if firstanswer in combinedOptions:
        if firstanswer in secondOptions:
            print("You're good! Here, take a cookie!")
            Score = Score + 1
            time.sleep(0.5)
        else:
            print("It's still easy. -_-")
            time.sleep(0.5)
    else:
        print("Don't try to fool me!")
        print("Restarting...")
        time.sleep(0.5)
        restart_program()

    print("Last question:")
    print("What is the 99th element on the periodic table?")
    print("A) Copper")
    print("B) Lutetium")
    print("C) Einsteinium")
    time.sleep(0.5)
    firstanswer = input("Answer: ")
    if firstanswer in combinedOptions:
        if firstanswer in thirdOptions:
            print("Admit it, you googled it.")
            Score = Score + 1
            time.sleep(0.5)
        else:
            print("That's ok, you're human.")
            time.sleep(0.5)
    else:
        print("Don't try to fool me!")
        print("Restarting...")
        time.sleep(0.5)
        restart_program()

    print("End of the game!")
    time.sleep(0.5)
    print("You scored " + str(Score) + " points.")
    sys.exit()
