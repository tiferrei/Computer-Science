#Elf Name Generator

#  Created by Tiago Ferreira on 16/12/2015.
#  Copyright (c) 2015 Tiago Ferreira. All rights reserved.


import time
import sys
UserReplay = True

positiveOptions = ["YES","yes","Yes","y","Y","Yup","yup","sim","s", "si", "sí", "Si", "Sí",
                   "Oui", "oui", "Ja", "ja", "Ken", "ken", "sea", "Sea", "Shah", "shah",
                   "Jes", "jes", "Hai", "hai", "Ndiyo", "ndiyo", "是", "Shi", "shi"] #Created Array for possitive options.

FirstElfNameArray = ["Sweetie","Jolly","Bubbles","Tootsie","Joyful","Sugar","Twinkle","Candy",
                "Merry","Huggy","Chipper","Angelic","Happy","Cookie","Sparkle","Jingle",
                "Bouncy","Delightful","Treacle","Sprinkles","Cupcake","Tinsel","Perky",
                "Precious","Sunny","Pinky"]

LastElfNameArray = ["Twinkle-Toes","Sugar-Plum","Sparkle-Pants","McJingles","Peppermint-Buns",
               "Sugar-Socks","Sprinkle-Pants","Angel-Ears","Sugar-Bells","Pointy-Toes",
               "McSprinkles","Candy-Canes"]

Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
            "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

Months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

while UserReplay == True:
    UserFirstName = input("Please enter your first name (John): ")
    UserMonth = input("Please enter your Month of birth (July): ")

    UserFirstLetter = UserFirstName[0]



    UserFirstLetterIndex = Letters.index(UserFirstLetter)
    UserMonthIndex = Months.index(UserMonth)

    FirstElfName = FirstElfNameArray[UserFirstLetterIndex]
    LastElfName = LastElfNameArray[UserMonthIndex]


    ElfName = FirstElfName + " " + LastElfName
    time.sleep(0.5)
    print("Your elf name is " + ElfName)
    time.sleep(0.5)

    WantsToReplay = input("Do you want to generate another elf name? ")

    if WantsToReplay in positiveOptions:
        time.sleep(1)
    else:
        print("Goodbye, " + ElfName + "!")
        time.sleep(1)
        sys.exit()
