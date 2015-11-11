#Binary Serach Game


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
        print("Is yor number", str(middle) + "?") #Print data for the user.
        IsMiddle = input("(YES, NO): ") #Ask data from the user, (to know if the number is the one in the middle).
        if IsMiddle in positiveOptions: #If the number is the one in the middle then do this.
            guessed = True #Mark as guessed to end the loop.
            print("Hurray! I did it!") #Celebrate :)
        else:                        #Else if the number is not the one in the middle do this.
            print("Is your number higher or lower than", str(middle) + "?") #Print information to the user.
            HigherOrLower = input("(Higher, Lower): ")  #Ask for data from the user.
            if HigherOrLower in higherOptions:  #Compare the data from the user to the 2 options. If true then:
                minimum = (middle + 1)  #The minimum is set to the current middle plus one.
            else:                       #If not:
                maximum = (middle - 1)  #The maximum is set to the current middle minus one.

    PlayAgain = input("Would you like to play again? (YES, NO): ") #Ask the user if he/she wnats to play again.

    if PlayAgain in positiveOptions: #Compare the answer from the user to th 2 options. If he/she wants to play again then:
        time.sleep(1)   #Wait one second
        guessed = False #Set guessed as False again to re-enter the loop.
    else:               #If not:
        print("Goodbye!") #Say Goodbye.
        time.sleep(1)     #Wait 1 second...
        sys.exit()        #And exit.
