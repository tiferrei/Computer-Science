#CSV Capitals

#  Created by Tiago Ferreira on 11/05/2016.
#  Copyright (c) 2016 Tiago Ferreira and Alex Butler

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import csv
import sys
import os
import time

capitalQuestions = []
hardQuestions = []
mediumQuestions = []
easyQuestions = []

with open ("Capitals.txt") as csvfile:
    capitalsCsv = csv.reader(csvfile, delimiter = ",")
    for row in capitalsCsv:
        capitalQuestions.append(row)
        if row[7] == "HARD":
            hardQuestions.append(row)
        elif row[7] == "MEDIUM":
            mediumQuestions.append(row)
        elif row[7] == "EASY":
            easyQuestions.append(row)
numberOfQuestions = len(capitalQuestions)
numberOfHardQuestions = len(hardQuestions)
numberOfMediumQuestions = len(mediumQuestions)
numberOfEasyQuestions = len(easyQuestions)

def allQuestionsFunc():
    points = 0
    for x in range(numberOfQuestions):
        print(capitalQuestions[x][1])
        print()
        print("A -> " + capitalQuestions[x][3])
        print("B -> " + capitalQuestions[x][4])
        print("C -> " + capitalQuestions[x][5])
        print("D -> " + capitalQuestions[x][6])
        print()
        userChoice = input("Answer (A, B, C, D): ")
        userChoice = userChoice.upper()
        if userChoice == capitalQuestions[x][2]:
            print("Correct!")
            points = points + 1
        else:
            print("Wrong!")
        time.sleep(2)
        print()
        os.system('clear')
    print("You scored " + str(points) + " points!")

def hardQuestionsFunc():
    hardPoints = 0
    for x in range(numberOfHardQuestions):
        print(hardQuestions[x][1])
        print()
        print("A -> " + hardQuestions[x][3])
        print("B -> " + hardQuestions[x][4])
        print("C -> " + hardQuestions[x][5])
        print("D -> " + hardQuestions[x][6])
        print()
        userChoice = input("Answer (A, B, C, D): ")
        userChoice = userChoice.upper()
        if userChoice == hardQuestions[x][2]:
            print("Correct!")
            hardPoints = hardPoints + 1
        else:
            print("Wrong!")
        time.sleep(2)
        print()
        os.system('clear')
    print("You scored " + str(hardPoints) + " points!")

def mediumQuestionsFunc():
    mediumPoints = 0
    for x in range(numberOfMediumQuestions):
        print(mediumQuestions[x][1])
        print()
        print("A -> " + mediumQuestions[x][3])
        print("B -> " + mediumQuestions[x][4])
        print("C -> " + mediumQuestions[x][5])
        print("D -> " + mediumQuestions[x][6])
        print()
        userChoice = input("Answer (A, B, C, D): ")
        userChoice = userChoice.upper()
        if userChoice == mediumQuestions[x][2]:
            print("Correct!")
            mediumPoints = mediumPoints + 1
        else:
            print("Wrong!")
        time.sleep(2)
        print()
        os.system('clear')
    print("You scored " + str(mediumPoints) + " points!")

def easyQuestionsFunc():
    easyPoints = 0
    for x in range(numberOfEasyQuestions):
        print(easyQuestions[x][1])
        print()
        print("A -> " + easyQuestions[x][3])
        print("B -> " + easyQuestions[x][4])
        print("C -> " + easyQuestions[x][5])
        print("D -> " + easyQuestions[x][6])
        print()
        userChoice = input("Answer (A, B, C, D): ")
        userChoice = userChoice.upper()
        if userChoice == easyQuestions[x][2]:
            print("Correct!")
            easyPoints = easyPoints + 1
        else:
            print("Wrong!")
        time.sleep(2)
        print()
        os.system('clear')
    print("You scored " + str(easyPoints) + " points!")

def menu():
    print("Welcome to the quiz! Choose an option below:")
    print()
    print("1 -> Easy questions")
    print("2 -> Medium questions")
    print("3 -> Hard questions")
    print("4 -> All questions")
    print("5 -> Quit")
    print()
    userSelection = input("Choose an option (1, 2, 3, 4, 5): ")
    time.sleep(2)
    if userSelection == "5":
        os.system('clear')
        sys.exit()
    elif userSelection == "4":
        os.system('clear')
        allQuestionsFunc()
    elif userSelection == "3":
        os.system('clear')
        hardQuestionsFunc()
    elif userSelection == "2":
        os.system('clear')
        mediumQuestionsFunc()
    elif userSelection == "1":
        os.system('clear')
        easyQuestionsFunc()
    else:
        print("Please choose a valid option.")
        os.system('clear')

menu()
