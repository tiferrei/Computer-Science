#Rock Paper Scissors Game

#  Created by Tiago Ferreira on 02/12/2015.
#  Copyright (c) 2015 Tiago Ferreira. All rights reserved.

import random
import sys
import time

positiveOptions = ["YES","yes","Yes","y","Y","Yup","yup","sim","s", "si", "sí", "Si", "Sí",
                   "Oui", "oui", "Ja", "ja", "Ken", "ken", "sea", "Sea", "Shah", "shah",
                   "Jes", "jes", "Hai", "hai", "Ndiyo", "ndiyo", "是", "Shi", "shi"]

ComputerOptions = ["Rock", "Paper", "Scissors"]
Paper = ["P", "p", "Paper", "paper"]
Rock = ["R", "r", "Rock", "rock"]
Scissors = ["S", "s", "Scissors", "scissors"]

UserScore = 0
ComputerScore = 0
UserTotal = 0
ComputerTotal = 0
Username = input("Hi there! What's your name? ")
print("Welcome " + Username + ", to the Rock Paper Scissors game!")
numberOfRounds = int(input("How many rounds would you like to play? "))

WantsToPlay = True
while WantsToPlay == True:



    IsReady = input("OK, are you ready? ") #Ask if the user is ready.
    if IsReady in positiveOptions or IsReady == "": #If yes then start the countdown.
        print("Starting game in...")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("GO!")
    else: #Otherwise:
        print("Goodbye.") #Say Goodbye.
        break #Break the loop.
        sys.exit() #Exit the program.

    for x in range(0,numberOfRounds):

        RandValue = random.randint(0,2)
        ComputerChoice = ComputerOptions[RandValue]

        UserInput = input("Paper, Rock or Scissors? ")
        if UserInput in Paper:
            UserChoice = "Paper"
        elif UserInput in Rock:
            UserChoice = "Rock"
        elif UserInput in Scissors:
            UserChoice = "Scissors"
        else:
            print("Don't try to fool me.")
            time.sleep(0.5)
            break
            sys.exit()

        if UserChoice == ComputerChoice:
            print("Tie!")
            time.sleep(0.5)
        elif UserChoice == "Rock" and ComputerChoice == "Paper":
            print("I won!")
            ComputerScore = ComputerScore + 1
            time.sleep(0.5)
        elif UserChoice == "Rock" and ComputerChoice == "Scissors":
            print("You won!")
            time.sleep(0.5)
            UserScore = UserScore + 1
        elif UserChoice == "Paper" and ComputerChoice == "Rock":
            print("You won!")
            time.sleep(0.5)
            UserScore = UserScore + 1
        #elif UserChoice == "Paper" and ComputerChoice == "Scissors":
        #    print("I won!")
        #    time.sleep(0.5)
        #    ComputerScore = ComputerScore + 1
        elif UserChoice == "Scissors" and ComputerChoice == "Rock":
            print("I won!")
            time.sleep(0.5)
            ComputerScore = ComputerScore + 1
        elif UserChoice == "Scissors" and ComputerChoice == "Paper":
            print("You won!")
            time.sleep(0.5)
            UserScore = UserScore + 1
        elif UserChoice == "Paper" and ComputerChoice == "Scissors":
            print("I won!")
            time.sleep(0.5)
            ComputerScore = ComputerScore + 1

    print("End of game!")
    time.sleep(0.5)

    if ComputerScore > UserScore:
        print("Aha! I won the game!")
        print("With a total of " + str(ComputerScore) + " points,")
        print("while you only scored " + str(UserScore) + ".")
    elif ComputerScore == UserScore:
        print("It's a tie!")
        print("We both scored a total of " + str(ComputerScore) + " points.")
    else:
        print("Wha! You won the game!")
        print("With a total of " + str(UserScore) + " points,")
        print("while I only scored " + str(ComputerScore) + ".")
        print("Congratulations, " + Username + "!")

    time.sleep(1)
    UserWantsToPlay = input("Do you want to play again? ")
    if UserWantsToPlay in positiveOptions:
        time.sleep(0.5)
    else:
        print("Goodbye, " + Username + "!")
        time.sleep(0.5)
        break
        sys.exit()
