#Summing Starter

#  Created by Tiago Ferreira on 01/02/2016.
#  Copyright (c) 2016 Tiago Ferreira. All rights reserved.

import random, sys #Import some modules

def summing(): #Define Summing
    GotItSumming = 0 #Initialize variable
    for x in range(1,6): #Loop for 5 times
        Number1 = random.randint(100, 500) #Generate random int
        Number2 = random.randint(100, 500) #Generate random int
        UserAnswer = int(input("What's the sum of " + str(Number1) + " and " + str(Number2) + "? ")) #Ask question
        Total = Number1 + Number2 #Get correct answer

        if UserAnswer == Total: #If the answer is correct:
            print("Well Done!") #Well done
            GotItSumming = GotItSumming + 1 #Add 1 point
        else: #Else:
            print("Wrong, the answer was " + str(Total)) #Give correct answer
    print("you got " + str(GotItSumming) + " questions right!") #At the end, say the number of correct answers

def multiplying(): #Define multiplying
    GotItMutliplying = 0 #Initialize varible
    for x in range(1,6): #Loop for 5 times
        Number1 = random.randint(2, 12) #Generate random number
        Number2 = random.randint(2, 12) #Generate random number
        UserAnswer = int(input("What's the multiplication of " + str(Number1) + " and " + str(Number2) + "? ")) #Ask question
        Total = Number1 * Number2 #Calculate correct answer

        if UserAnswer == Total: #
            print("Well Done!")
            GotItMutliplying = GotItMutliplying + 1
        else:
            print("Wrong, the answer was " + str(Total))
    print("you got " + str(GotItMutliplying) + " questions right!")

def Quiz():
    while 1 == 1:
        IsValid = False
        while IsValid == False:
            print()
            print("""What do you want to do?
            A -> Addition Quiz
            B -> multiplication Quiz
            Q -> Quit""")

            UserChoice = input("(A, B or Q): ")

            if UserChoice == "Q":
                IsValid = True
                sys.exit()
            elif UserChoice == "A":
                IsValid = True
                summing()
            elif UserChoice == "B":
                IsValid = True
                multiplying()
            else:
                print("Ivalid, please enter A, B or Q")
                IsValid = False

Quiz()
