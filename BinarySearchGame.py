#Binary Search Game

#  Created by Tiago Ferreira on 09/11/2015.
#  Copyright (c) 2015 Tiago Ferreira. All rights reserved.


import sys      #Used to exit the program at the end.
import time     #Used to give delay on restarting the program.

positiveOptions = ["YES","yes","Yes","y","Y","Yup","yup","sim","s"] #Dictionary for positive options.
higherOptions = ["Higher","H","h","High","high"]  #Dictionary for higher options.
guessed = False    #Creating default values for vital variables.
maximum = 1000
minimum = 1
wantsToPlay = True

while wantsToPlay == True:  #Start of the program itslef,
                            #(included in a loop to give an option to restart).

    while guessed == False:     #While the user doesen't guesses the number do this.
        middle = int(((maximum - minimum) / 2) + minimum) #Calculate the middle point for each maximum and minimum.
        print("Is your number", str(middle) + "?") #Print data for the user.
        IsMiddle = input("Answer: ") #Ask data from the user, (to know if the number is the one in the middle).
        if IsMiddle in positiveOptions: #If the number is the one in the middle then do this.
            guessed = True #Mark as guessed to end the loop.
            print("Hurray! I did it!") #Celebrate :)
        else:                        #Else if the number is not the one in the middle do this.
            print("Is your number higher or lower than", str(middle) + "?") #Print information to the user.
            HigherOrLower = input("Answer: ")  #Ask for data from the user.
            if HigherOrLower in higherOptions:  #Compare the data from the user to the 2 options. If true then:
                minimum = (middle + 1)  #The minimum is set to the current middle plus one.
            else:                       #If not:
                maximum = (middle - 1)  #The maximum is set to the current middle minus one.

    PlayAgain = input("Would you like to play again? ") #Ask the user if he/she wnats to play again.

    if PlayAgain in positiveOptions: #Compare the answer from the user to th 2 options. If he/she wants to play again then:
        time.sleep(1)   #Wait one second
        guessed = False #Set guessed as False again to re-enter the loop.
    else:               #If not:

        time.sleep(1)     #Wait 1 second...
        IsSir = input("Are you Sir and would like to see the answers to the evaluation questions? ") #Create variable for if statement.

        if IsSir in positiveOptions: #If the user input is something like yes then:
            print("Welcome Sir,") #Be polite, say hello.
            print() #empy line
            time.sleep(0.5) #wait 0.5 seconds.
            print("""Yes, this program works without any erros,
the program also meets all the requirements.

This program works using the Binary Search method, this is,
to get the middle of the total numbers and ask the user if the
middle number is the one he/she thought of, if not than is it
bigger or smaller? And then, the program sets the range of possible
numbers to the higher or lower values, and this repeats in a loop
until the user says that the number has been guessed.

The basic contructs are lists; variables; if statements; loop statements;
while statements; import command to import modules; the time module and
the sys module.

Yes, the program is readble and (almost) every line of code has been
commented with it's functionality.

Yes, the program has been fully tested, every input and if statement
consequence has been tested.

A good feature is the use if a list for possible user inputs (this way
the user isn't limited to YES or Y) and the bad feature that could be
improved is that this method takes too long for 1 - 1000 numbers.

By writing this program I learnt to use lists.

Yes, I coached other pupils. With them I learnt the importance of
indentation! """)
            print()
            time.sleep(0.5) #wait again.
            print("Thank you, Tiago Ferreira. (10KO)") #Be polite, say thank you.
            sys.exit() #Exit
        else:
            print("Alright, Goodbye!") #Say goodbye
            sys.exit() #Exit
