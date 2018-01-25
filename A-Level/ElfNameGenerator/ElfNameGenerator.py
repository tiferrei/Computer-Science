#  Elf Name Generator

#  Created by Tiago Ferreira on 04/12/2017.
#  Copyright (c) 2017 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import sys
from string import ascii_uppercase

def readNames(filePath):
    names = []
    with open(filePath, "r") as file:
        for line in file:
            names.append(line.split())
    return names

def readElves():
    elves = []
    with open("elves.txt", "r") as file:
        for line in file:
            elves = eval(line)
    return elves

def writeNames(names, filePath):
    with open(filePath, "w") as file:
        for name in names:
            file.write(name[0] + " " + name[1] + "\n")

def menu():
    print("Welcome!")
    print("Please pick an option:")
    print("1. Convert a name to an elf name.")
    print("2. Convert an elf name to a name.")
    print("3. Quit")

    userSelection = int(input("Please enter a number (1, 2, 3): "))
    if userSelection == 1:
        name = nameToElf(input("Enter your first name: "), input("Enter your last name: "))
        print("Your Elf name is: " + name[0] + " " + name[1])
    elif userSelection == 2:
        elfToName()
    else:
        sys.exit()

def nameToElf(firstName, lastName):
    firstName = firstName.upper()
    lastName = lastName.upper()
    firstIndex =  ascii_uppercase.index(firstName[0])
    lastIndex =  ascii_uppercase.index(lastName[0])
    elves = readElves()
    return(elves[firstIndex][0], elves[lastIndex][1])

def elfToName():
    inputFilePath = input("Enter input file path: ")
    outputFilePath = input("Enter ouput file path: ")
    names = readNames(inputFilePath)
    newNames = []
    for name in names:
        newNames.append(nameToElf(name[0], name[1]))
    writeNames(newNames, outputFilePath)

menu()
