#Elf Name Generator

#  Created by Tiago Ferreira on 16/12/2015.
#  Copyright (c) 2015 Tiago Ferreira. All rights reserved.

import sys
import random
import time


FirstElfNameArray = ["Sweetie","Jolly","Bubbles","Tootsie","Joyful","Sugar","Twinkle","Candy",
                "Merry","Huggy","Chipper","Angelic","Happy","Cookie","Sparkle","Jingle",
                "Bouncy","Delightful","Treacle","Sprinkles","Cupcake","Tinsel","Perky",
                "Precious","Sunny","Pinky"]

LastElfNameArray = ["Twinkle-Toes","Sugar-Plum","Sparkle-Pants","McJingles","Peppermint-Buns",
               "Sugar-Socks","Sprinkle-Pants","Angel-Ears","Sugar-Bells","Pointy-Toes",
               "McSprinkles","Candy-Canes"]

Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
            "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


UserFirstName = input("Please enter your first name: ")
UserLastName = input("Please enter your last name: ")

UserFirstLetter = UserFirstName[0]
UserLastLetter = UserLastName[0]

UserFirstLetterIndex = Letters.index(UserFirstLetter)
UserLastLetterIndex = Letters.index(UserLastLetter)

FirstElfName = FirstElfNameArray[UserFirstLetterIndex]
LastElfName = LastElfNameArray[UserLastLetterIndex]


ElfName = FirstElfName + " " + LastElfName
print("Your elf name is " + ElfName)
