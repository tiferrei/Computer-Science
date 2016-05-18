#CSV Car Sales

#  Created by Tiago Ferreira on 18/05/2016.
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

carList = []

with open ("CarSales.txt") as csvfile:
    carsCsv = csv.reader(csvfile, delimiter = ",")
    for row in carsCsv:
        carList.append(row)

listLength = len(carList)

def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def find(l, element):
    for row, i in enumerate(l):
        try:
            column = i.index(element)
        except ValueError:
            continue
        return row
    return -1

def menu():
    print()
    print("Welcome to the car sales database, please choose an option:")
    print()
    print("1 - Print all data.")
    print("2 - Print sales from September 2014.")
    print("3 - Print sales from September 2015.")
    print("4 - Print sales from January 2014 to September 2014.")
    print("5 - Print sales from January 2015 to September 2015.")
    print("6 - Select a car brand to display data.")
    print("7 - Quit.")
    print()
    userChoice = input("Option selected (1, 2, 3, 4, 5, 6): ")
    os.system('clear')
    delay_print("Loading Data...")
    print()
    time.sleep(0.5)
    if userChoice == "1":
        allData()
    elif userChoice == "2":
        sep14()
    elif userChoice == "3":
        sep15()
    elif userChoice == "4":
        sj14()
    elif userChoice == "5":
        sj15()
    elif userChoice == "6":
        selectCar()
    elif userChoice == "7":
        quit()

def allData():
    print("+------------------------------------------+")
    print("|{0:14}|{1:6}|{2:6}|{3:6}|{4:6}|".format("Car Brand", "Sep 15", "Sep 14", "J-S 15", "J-S 14"))
    print("+------------------------------------------+")
    for i in range(listLength):
        print("|{0:14}|{1:6}|{2:6}|{3:6}|{4:6}|".format(carList[i][0], carList[i][1], carList[i][2], carList[i][3], carList[i][4]))
        time.sleep(0.05)
    print("+------------------------------------------+")

def sep14():
    print("+---------------------+")
    print("|{0:14}|{1:6}|".format("Car Brand", "Sep 14"))
    print("+---------------------+")
    for i in range(listLength):
        print("|{0:14}|{1:6}|".format(carList[i][0], carList[i][2]))
    print("+---------------------+")

def sep15():
    print("+---------------------+")
    print("|{0:14}|{1:6}|".format("Car Brand", "Sep 15"))
    print("+---------------------+")
    for i in range(listLength):
        print("|{0:14}|{1:6}|".format(carList[i][0], carList[i][1]))
    print("+---------------------+")

def sj14():
    print("+---------------------+")
    print("|{0:14}|{1:6}|".format("Car Brand", "S-J 14"))
    print("+---------------------+")
    for i in range(listLength):
        print("|{0:14}|{1:6}|".format(carList[i][0], carList[i][4]))
    print("+---------------------+")

def sj15():
    print("+---------------------+")
    print("|{0:14}|{1:6}|".format("Car Brand", "S-J 15"))
    print("+---------------------+")
    for i in range(listLength):
        print("|{0:14}|{1:6}|".format(carList[i][0], carList[i][3]))
    print("+---------------------+")

def selectCar():
    userSelected = input("Please enter a car brand (Land Rover): ")
    nameIndex = find(carList, userSelected)
    print("+------------------------------------------+")
    print("|{0:14}|{1:6}|{2:6}|{3:6}|{4:6}|".format("Car Brand", "Sep 15", "Sep 14", "J-S 15", "J-S 14"))
    print("+------------------------------------------+")
    print("|{0:14}|{1:6}|{2:6}|{3:6}|{4:6}|".format(carList[nameIndex][0], carList[nameIndex][1], carList[nameIndex][2], carList[nameIndex][3], carList[nameIndex][4]))
    print("+------------------------------------------+")


def quit():
    delay_print("Terminating system.")
    sys.exit()

#menu()
selectCar()
