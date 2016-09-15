#  Controlled Assessment
#  Created by Tiago Ferreira on 15/09/2016.
#  Copyright (c) 2016 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import sys, os, time, random

employeeID = []
name = []
phoneNumber = []
qualification = []

def menu():
    print("Welcome Caroline!")
    print()
    print("Available options:")
    print("A -> Register new employee")
    choise = input("Please select an option (A): ")
    if choise == "A":
        registerNewEmployee()

def registerNewEmployee():
    informationIsIncorrect = True
    while informationIsIncorrect:
        idInput = input("Please enter an employee ID: ")
        nameInput = input("Please enter the employee's name: ")
        phoneNumberInput = input("Please enter the employee's phone number: ")
        qualificationInput = input("Please enter the employee's qualification (AP, FQ): ")
        while qualificationInput != "AP" and qualificationInput != "FQ":
            print("Enter only 'AP' for apprentice or 'FQ' for fully-qualified.")
            qualificationInput = input("Please enter the employee's qualification (AP, FQ): ")
        print()
        print("New employee's details:")
        print("ID: " + str(idInput))
        print("Name: " + str(nameInput))
        print("Phone Number: " + str(phoneNumberInput))
        if qualificationInput == "AP":
            print("Qualification: Apprentice")
        elif qualificationInput == "FQ":
            print("Qualification: Fully-qualified")
        else:
            print("###DEBUG### FOUND INVALID INPUT: " + str(qualificationInput))
        print()
        isCorrect = input("Is the above information correct (YES, NO)? ")
        if isCorrect == "YES":
            employeeID.append(idInput)
            name.append(nameInput)
            phoneNumber.append(phoneNumberInput)
            qualification.append(qualificationInput)
            informationIsIncorrect = False
    menu()

menu()
