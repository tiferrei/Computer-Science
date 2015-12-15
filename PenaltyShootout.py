#Forename and Surname

#  Created by Tiago Ferreira on 07/12/2015.
#  Copyright (c) 2015 Tiago Ferreira. All rights reserved.

import random
import sys
import time

High = ["H", "h", "High", "high"]
Low = ["L", "l", "low", "Low"]
Left = ["L", "l", "Left", "left"]
Centre = ["C", "c", "Centre", "centre"]
Right = ["R", "r", "right", "Right"]
ComputerHightOptions = ["High", "Low"]
ComputerWidthOptions = ["Left", "Center", "Right"]
KickerOptions = ["kicker", "k", "K", "Kicker"]
SaveWidthOptions = ["Left", "Centre", "Right"]
SaveHeightOptions = ["High", "Low"]
GoalkeeperOptions = ["goalkeeper", "g", "G", "Goalkeeper"]
Goals = 0
ComputerGoals = 0
savedGoals = 0
UserSavedGoals = 0


print("Helo there!")
goalkeeperOrKicker = input("Do you want to start by being the kicker or the goalkeeper? ")

if goalkeeperOrKicker in KickerOptions:
    for x in range(5):

        KickWidthInput = input("Where to do you want to kick the ball? (Left, Centre, Right): ")
        KickHightInput = input("Where to do you want to kick the ball? (High, Low): ")

        if KickHightInput in High:
            KickHight = "High"
        elif KickHightInput in Low:
            KickHight = "Low"
        else:
            print("Don't try to fool me!")
            sys.exit()

        if KickWidthInput in Left:
            KickWidth = "Left"
        elif KickWidthInput in Centre:
            KickWidth = "Centre"
        elif KickWidthInput in Right:
            KickWidth = "Right"
        else:
            print("Don't try to fool me!")
            sys.exit()

        ComputerRanHight = random.randint(0,1)
        ComputerRanWidth = random.randint(0,2)

        ComputerHight = ComputerHightOptions[ComputerRanHight]
        ComputerWidth = ComputerWidthOptions[ComputerRanWidth]

        if ComputerWidth == KickWidth and ComputerHight == KickHight:
            print()
            print("You kicked to " + KickHight + " and " + KickWidth + ".")
            print("While I went to " + ComputerHight + " and " + ComputerWidth + ".")
            print()
            print("Save! Aha!")
            savedGoals = savedGoals + 1
        else:
            print()
            print("You kicked to " + KickHight + " and " + KickWidth + ".")
            print("While I went to " + ComputerHight + " and " + ComputerWidth + ".")
            print()
            print("Gooooooal!")
            Goals = Goals + 1

    print("End of game!")
    print("You made " + str(Goals) + " goals.")
    print("I saved " + str(savedGoals) + " goals.")
    time.sleep(1)
    print("Now let's extange roles!")
    time.sleep(0.5)

    for x in range(5):

        SaveWidthInput = input("Where to do you want to kick the ball? (Left, Centre, Right): ")
        SaveHightInput = input("Where to do you want to kick the ball? (High, Low): ")

        if SaveHightInput in High:
            SaveHight = "High"
        elif SaveHightInput in Low:
            SaveHight = "Low"
        else:
            print("Don't try to fool me!")
            sys.exit()

        if SaveWidthInput in Left:
            SaveWidth = "Left"
        elif SaveWidthInput in Centre:
            SaveWidth = "Centre"
        elif KickWidthInput in Right:
            SaveWidth = "Right"
        else:
            print("Don't try to fool me!")
            sys.exit()

        ComputerRanHight = random.randint(0,1)
        ComputerRanWidth = random.randint(0,2)

        ComputerHight = ComputerHightOptions[ComputerRanHight]
        ComputerWidth = ComputerWidthOptions[ComputerRanWidth]

        if ComputerWidth == SaveWidth and ComputerHight == SaveHight:
            print()
            print("I kicked to " + ComputerHight + " and " + ComputerWidth + ".")
            print("While you went to " + SaveHight + " and " + SaveWidth + ".")
            print()
            print("Save! I failed!")
            UserSavedGoals = UserSavedGoals + 1
        else:
            print()
            print("I kicked to " + ComputerHight + " and " + ComputerWidth + ".")
            print("While you went to " + SaveHight + " and " + SaveWidth + ".")
            print()
            print("Gooooooal! I did it!")
            ComputerGoals = ComputerGoals + 1

    print("End of game!")
    print("I made " + str(Goals) + " goals.")
    print("You saved " + str(UserSavedGoals) + " goals.")


elif goalkeeperOrKicker in GoalkeeperOptions:

    for x in range(5):

        SaveWidthInput = input("Where do you want to go to save the ball? (Left, Centre, Right): ")
        SaveHightInput = input("Where do you want to go to save the ball? (High, Low): ")

        if SaveHightInput in High:
            SaveHight = "High"
        elif SaveHightInput in Low:
            SaveHight = "Low"
        else:
            print("Don't try to fool me!")
            sys.exit()

        if SaveWidthInput in Left:
            SaveWidth = "Left"
        elif SaveWidthInput in Centre:
            SaveWidth = "Centre"
        elif SaveWidthInput in Right:
            SaveWidth = "Right"
        else:
            print("Don't try to fool me!")
            sys.exit()

        ComputerRanHight = random.randint(0,1)
        ComputerRanWidth = random.randint(0,2)

        ComputerHight = ComputerHightOptions[ComputerRanHight]
        ComputerWidth = ComputerWidthOptions[ComputerRanWidth]

        if ComputerWidth == SaveWidth and ComputerHight == SaveHight:
            print()
            print("I kicked to " + ComputerHight + " and " + ComputerWidth + ".")
            print("While you went to " + SaveHight + " and " + SaveWidth + ".")
            print()
            print("Save! I failed!")
            UserSavedGoals = UserSavedGoals + 1
        else:
            print()
            print("I kicked to " + ComputerHight + " and " + ComputerWidth + ".")
            print("While you went to " + SaveHight + " and " + SaveWidth + ".")
            print()
            print("Gooooooal! I did it!")
            ComputerGoals = ComputerGoals + 1

    print("End of game!")
    print("I made " + str(ComputerGoals) + " goals.")
    print("You saved " + str(UserSavedGoals) + " goals.")
    print()
    print("Now let's exchange roles!")
    time.sleep(1)

    for x in range(5):

        KickWidthInput = input("Where to do you want to kick the ball? (Left, Centre, Right): ")
        KickHightInput = input("Where to do you want to kick the ball? (High, Low): ")

        if KickHightInput in High:
            KickHight = "High"
        elif KickHightInput in Low:
            KickHight = "Low"
        else:
            print("Don't try to fool me!")
            sys.exit()

        if KickWidthInput in Left:
            KickWidth = "Left"
        elif KickWidthInput in Centre:
            KickWidth = "Centre"
        elif KickWidthInput in Right:
            KickWidth = "Right"
        else:
            print("Don't try to fool me!")
            sys.exit()

        ComputerRanHight = random.randint(0,1)
        ComputerRanWidth = random.randint(0,2)

        ComputerHight = ComputerHightOptions[ComputerRanHight]
        ComputerWidth = ComputerWidthOptions[ComputerRanWidth]

        if ComputerWidth == KickWidth and ComputerHight == KickHight:
            print()
            print("You kicked to " + KickHight + " and " + KickWidth + ".")
            print("While I went to " + ComputerHight + " and " + ComputerWidth + ".")
            print()
            print("Save! Aha!")
            savedGoals = savedGoals + 1
        else:
            print()
            print("You kicked to " + KickHight + " and " + KickWidth + ".")
            print("While I went to " + ComputerHight + " and " + ComputerWidth + ".")
            print()
            print("Gooooooal!")
            Goals = Goals + 1



else:
    print("Dont try to fool me!")
    sys.extit()
