#  Files

#  Created by Tiago Ferreira on 21/09/2017.
#  Copyright (c) 2017 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import sys

def main():
    print()
    print("Welcome, there are 3 options:")
    print("1 Enter and save new data")
    print("2 Load and display data")
    print("3 Quit")
    print()

    userChoice = 0
    while userChoice != 1 and userChoice != 2 and userChoice != 3:
        userChoice = int(input("Choice (1, 2, 3): "))

    if userChoice == 1:
        enterData()
    elif userChoice == 2:
        loadData()
    elif userChoice == 3:
        sys.exit()

def writeToFile(school):
    with open("database.txt", 'a') as db:
        for element in school:
            db.write("%s " % element)
        db.write("\n")

def readToList():
    schools = []
    with open("database.txt", 'r') as db:
        for line in db:
            schools.append(line.split())
    return schools

def askForWins():
    numberOfWins = 0
    while True:
        try:
            numberOfWins = int(input("Enter number of wins (0 - 20): "))
            if numberOfWins not in range(0, 21):
                raise ValueError('Not in valid range')
        except ValueError:
            print("Sorry, that number is invalid.")
            continue
        else:
            break
    return numberOfWins

def askForDraws():
    numberOfDraws = 0
    while True:
        try:
            numberOfDraws = int(input("Enter number of draws (0 - 20): "))
            if numberOfDraws not in range(0, 21):
                raise ValueError('Not in valid range')
        except ValueError:
            print("Sorry, that number is invalid.")
            continue
        else:
            break
    return numberOfDraws

def askForLoses():
    numberOfLoses = 0
    while True:
        try:
            numberOfLoses = int(input("Enter number of loses (0 - 20): "))
            if numberOfLoses not in range(0, 21):
                raise ValueError('Not in valid range')
        except ValueError:
            print("Sorry, that number is invalid.")
            continue
        else:
            break
    return numberOfLoses

def enterData():
    school = []
    name = input("Enter the school name: ")
    school.append(name)
    school.append(askForWins())
    school.append(askForDraws())
    school.append(askForLoses())
    writeToFile(school)
    main()

def loadData():
    schools = readToList()
    if not schools:
        print("There are no records in the DB.")
    else:
        for school in schools:
            print("School: " + school[0])
            print("    Wins: " + school[1])
            print("    Draws: " + school[2])
            print("    Loses: " + school[3])
        main()

main()
