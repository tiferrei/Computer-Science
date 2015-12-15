#Forename and Surname

#  Created by Tiago Ferreira on 07/12/2015.
#  Copyright (c) 2015 Tiago Ferreira. All rights reserved.

<<<<<<< HEAD
import random #import random library
import sys #import sys library
import time #import time library

High = ["H", "h", "High", "high"] #Define High options
Low = ["L", "l", "low", "Low"] #Define Low options.
Left = ["L", "l", "Left", "left"] #Define left options
Centre = ["C", "c", "Centre", "centre"] #Define Centre options.
Right = ["R", "r", "right", "Right"] #Define right options.
ComputerHightOptions = ["High", "Low"] #Define the computer options for the Hight.
ComputerWidthOptions = ["Left", "Center", "Right"] #Define the computer options for the width.
KickerOptions = ["kicker", "k", "K", "Kicker"] #Define the options for the kicker.
SaveWidthOptions = ["Left", "Centre", "Right"] #Define the options for the goalkeeper width.
SaveHeightOptions = ["High", "Low"] #Define the options for the goalkeeper height.
GoalkeeperOptions = ["goalkeeper", "g", "G", "Goalkeeper"] #Define the options for Goalkeeper.
Goals = 0 #Define Goals as 0.
ComputerGoals = 0 #Define ComputerGoals as 0.
SavedGoals = 0 #Define SavedGoals as 0.
UserSavedGoals = 0 #Define UserSavedGoals as 0.


print("Helo there!") #Welcome de user.
GoalkeeperOrKicker = input("Do you want to start by being the kicker or the goalkeeper? ") #Ask for Goalkeeper or Kicker.

if GoalkeeperOrKicker in KickerOptions: #If Kicker, then:
    for x in range(5): #Do this 5 times:

        KickWidthInput = input("Where to do you want to kick the ball? (Left, Centre, Right): ") #Ask for
=======
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


print("Hello there!")
time.sleep(0.5)
goalkeeperOrKicker = input("Do you want to start by being the kicker or the goalkeeper? ")

if goalkeeperOrKicker in KickerOptions:
    for x in range(5):

        KickWidthInput = input("Where to do you want to kick the ball? (Left, Centre, Right): ")
>>>>>>> origin/master
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
            SavedGoals = SavedGoals + 1
        else:
            print()
            print("You kicked to " + KickHight + " and " + KickWidth + ".")
            print("While I went to " + ComputerHight + " and " + ComputerWidth + ".")
            print()
            print("Gooooooal!")
            Goals = Goals + 1

    print("End of game!")
    print("You made " + str(Goals) + " goals.")
    print("I saved " + str(SavedGoals) + " goals.")
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


elif GoalkeeperOrKicker in GoalkeeperOptions:

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
            SavedGoals = SavedGoals + 1
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
    
