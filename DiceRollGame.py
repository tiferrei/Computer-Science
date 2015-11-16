import random
import sys
import time
positiveOptions = ["YES","yes","Yes","y","Y","Yup","yup","sim","s"]
WantsToPlay = True
ComputerTotal = 0
UserTotal = 0
ComputerScore = 0
UserScore = 0
dice1 = 0
dice2 = 0
dice3 = 0
dice4 = 0
dice5 = 0
dice6 = 0


while WantsToPlay == True:
    name = input("Hi! What's your name? ")
    time.sleep(0.5)
    print("Welcome " + name + ", to the Dice Roll Game!")
    WantsTutorial = input("Would you like to go through the tutorial? ")
    if WantsTutorial in positiveOptions:
        print("""Alright, so basically we'll play Dice Roll, a game in which
each of use gets 3 dices, we throw them and the one who has the biggest sum
wins! There will be 5 rounds... """)
        time.sleep(0.5)
        print()
    else:
        print("Alright...")
        time.sleep(0.5)
    IsReady = input("Ready? ")
    if IsReady in positiveOptions:
        print("Starting game in...")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("GO!")
    else:
        print("Goodbye, " + name + ".")
        break
        sys.exit()
    for x in range(1,6):
        print("Rolling dices...")
        time.sleep(0.5)
        dice1 = random.randint(1,7)
        dice2 = random.randint(1,7)
        dice3 = random.randint(1,7)
        dice4 = random.randint(1,7)
        dice5 = random.randint(1,7)
        dice6 = random.randint(1,7)
        print("Summing...")
        time.sleep(0.5)
        ComputerTotal = (dice1 + dice2 + dice3)
        UserTotal = (dice4 + dice5 + dice6)
        print("Comparing totals....")
        time.sleep(0.5)
        if ComputerTotal > UserTotal:
            print("I won this round!")
            print("(" + str(ComputerTotal) + " > " + str(UserTotal) + ")")
            ComputerScore = ComputerScore + 1
        elif ComputerTotal < UserTotal:
            print("You won this round!")
            print("(" + str(ComputerTotal) + " < " + str(UserTotal) + ")")
            UserScore = UserScore + 1
        elif ComputerScore == UserScore:
            print("Draw!")
    print("The game is over!")
    if ComputerScore == UserScore:
        print("It's a draw!")
        print("(" + str(ComputerScore) + " = " + str(UserScore) + ")")
    elif ComputerScore > UserScore:
        print("I won the game!")
        print("(" + str(ComputerScore) + " > " + str(UserScore) + ")")
    elif ComputerScore < UserScore:
        print("You won the game!")
        print("(" + str(ComputerScore) + " < " + str(UserScore) + ")")
    UserWantsToPlay = input("Do you want to play again, " + name + "? ")
    if UserWantsToPlay in positiveOptions:
        WantsToPlay = True
    else:
        WantsToPlay = False
        print("Goodbye, " + name + ".")
        time.sleep(0.5)
        sys.exit()
