#  Unit 1

#  Created by Tiago Ferreira on 03/10/2017.
#  Copyright (c) 2017 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import csv

def displayMenu():
    print()
    print("1. Enter data")
    print("2. Find max population")
    print("3. Quit")
    print()
    choice = int(input("Enter your choice: "))
    return choice

def enterData():
    townFile = input("Enter file name: ")
    with open(townFile, "a") as file:
        town = input("Enter town name: ")
        while town != "xxx":
            county = input("Enter county: ")
            population = input("Enter population: ")
            file.write(county + "," + town + "," + population + "\n")
            town = input("Enter town name: ")

def findMax():
    townFile = input("Enter file name: ")
    maxPop = 0
    maxTown = ""
    with open(townFile, "r") as file:
        for rawLine in file:
            line = rawLine.split(",")
            if int(line[2]) > maxPop:
                maxTown = line[1]
                maxPop = int(line[2])
    print(maxTown + " is the biggest city with " + str(maxPop) + " citizens.")

def main():
    choice = 0
    while choice != 3:
        choice = displayMenu()
        if choice == 1:
            enterData()
        elif choice == 2:
            findMax()
    print("Program Ended")

main()
