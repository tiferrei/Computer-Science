#  Controlled Assessment 2
#  Created by Tiago Ferreira on 13/10/2016.
#  Copyright (c) 2016 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import csv, sys

def menu(): # Menu declaration
    print("Welcome Caroline!")
    print()
    print("Available options:")
    print("A -> Search for an estimate")
    print("B -> Display outstanding payments")
    print("C -> Display total revenue")
    print("Q –> Quit")
    choise = input("Please select an option (A, B, C): ")

    populateDatabase()

    if choise == "A":
        searchForEstimate() # Call to searchForEstimate function.
    elif choise == "B":
        displayOutstandingPayments() # Call to displayOutstandingPayments function.
    elif choise == "C":
        displayTotalRevenue() # Call to displayTotalRevenue function.
    elif coise == "Q":
        sys.exit() # Exit
    else:
        print("Please enter an available option (A, B, C).")

def searchForEstimate():
    global database
    estID = input("Please enter an Eestimate ID: ")
    print("Searching for estimate " + str(estID) + "...")
    foundEstimate = False
    for record in range(len(database)):
        if database[record][0] == estID:
            foundEstimate = True
            print("Found estimate " + str(estID) + ":")
            print("Estimate Number: " + str(database[record][0]))
            print("Customer ID: " + str(database[record][2]))
            print("Final Amount: " + str(database[record][3]))
            print("Amount Paied: " + str(database[record][5]))
            print("Estimate Date: " + str(database[record][1]))
            if str(database[record][4]) == "E":
                print("Status: Estimate")
            elif str(database[record][4]) == "A":
                print("Status: Accepted Job")
            elif str(database[record][4]) == "N":
                print("Status: Not Accepted")
    if foundEstimate == False:
        print("Sorry. No estimate found for ID: " + str(estID))

# Helper functions
def populateDatabase():
    with open("paintingJobs.txt", "r") as theFile:
        global database
        database = []
        for line in theFile:
            line = line.strip('\n')
            line = line.strip('\t')
            database.append(line.split(",")) #Add line to database

menu() # Start program.
