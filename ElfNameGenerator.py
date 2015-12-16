#Elf Name Generator

#  Created by Tiago Ferreira on 16/12/2015.
#  Copyright (c) 2015 Tiago Ferreira. All rights reserved.


import time
import sys
UserReplay = True

positiveOptions = ["YES","yes","Yes","y","Y","Yup","yup","sim","s", "si", "sí", "Si", "Sí",
                   "Oui", "oui", "Ja", "ja", "Ken", "ken", "sea", "Sea", "Shah", "shah",
                   "Jes", "jes", "Hai", "hai", "Ndiyo", "ndiyo", "是", "Shi", "shi"] #Created Array for possitive options.

FirstElfNameArray = ["Sweetie","Jolly","Bubbles","Tootsie","Joyful","Sugar","Twinkle","Candy", #Created Array for Elf first names.
                "Merry","Huggy","Chipper","Angelic","Happy","Cookie","Sparkle","Jingle",
                "Bouncy","Delightful","Treacle","Sprinkles","Cupcake","Tinsel","Perky",
                "Precious","Sunny","Pinky"]

LastElfNameArray = ["Twinkle-Toes","Sugar-Plum","Sparkle-Pants","McJingles","Peppermint-Buns", #Created Array for Elf last name.
               "Sugar-Socks","Sprinkle-Pants","Angel-Ears","Sugar-Bells","Pointy-Toes",
               "McSprinkles","Candy-Canes"]

Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", #Created Array for possible letters.
            "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

Months = ["January", "February", "March", "April", "May", "June", "July", #Created Array for months.
          "August", "September", "October", "November", "December"]

while UserReplay == True: #Initiate loop.
    UserFirstName = input("Please enter your first name (John): ") #Ask for first name.
    UserMonth = input("Please enter your Month of birth (July): ") #Ask for month of birth.

    UserFirstLetter = UserFirstName[0] #Get the first letter of name.



    UserFirstLetterIndex = Letters.index(UserFirstLetter) #Index it.
    UserMonthIndex = Months.index(UserMonth) #Get Index for month.

    FirstElfName = FirstElfNameArray[UserFirstLetterIndex] #Generate First elf name.
    LastElfName = LastElfNameArray[UserMonthIndex] #Generate Last elf name.


    ElfName = FirstElfName + " " + LastElfName #Combine them into one string.
    time.sleep(0.5) #A bit of delay.
    print("Your elf name is " + ElfName) #Prin the name.
    time.sleep(0.5) #Another bit of delay.

    WantsToReplay = input("Do you want to generate another elf name? ") #Ask if the user wants to replay.

    if WantsToReplay in positiveOptions: #If yes,
        time.sleep(1) #Wait a sencond and restart.
    else: #If not,
        print("Goodbye, " + ElfName + "!") #Say Goodbye.
        time.sleep(1) #Wait a second.
        sys.exit() #Exit.
