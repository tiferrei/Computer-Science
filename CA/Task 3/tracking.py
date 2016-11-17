#  Controlled Assessment 3
#  Created by Tiago Ferreira on 13/10/2016.
#  Copyright (c) 2016 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import csv, sys, time

def menu(): # Menu declaration
    print("Welcome Caroline!")
    print()
    print("Available options:")
    print("A -> Search for an estimate")
    print("B -> Display outstanding payments")
    print("C -> Display total revenue")
    print("Q –> Quit")
    choise = input("Please select an option (A, B, C): ")

    populateDatabase() # Function that reads data from the textfile.

    if choise == "A":
        searchForEstimate() # Call to searchForEstimate function.
    elif choise == "B":
        displayOutstandingPayments() # Call to displayOutstandingPayments function.
    elif choise == "C":
        displayTotalRevenue() # Call to displayTotalRevenue function.
    elif choise == "Q":
        sys.exit() # Exit
    else:
        print("Please enter an available option (A, B, C, Q).")
        menu()

def searchForEstimate(): # Declaring a function to search for an estimate
    global database # Initialise Database instanse.
    estID = input("Please enter an Eestimate ID: ") # Get the ID from the user
    print("Searching for estimate " + str(estID) + "...")
    foundEstimate = False
    for record in range(len(database)): # Repeat for each record in the database.
        if database[record][0] == estID: # If that record matches the ID,
            foundEstimate = True # Signalise it
            print("Found estimate " + str(estID) + ":")
            print("Estimate Number: " + str(database[record][0])) # Print data from that record.
            print("Customer ID: " + str(database[record][2])) # Print data from that record.
            print("Final Amount: " + str(database[record][3])) # Print data from that record.
            print("Amount Paied: " + str(database[record][5])) # Print data from that record.
            print("Estimate Date: " + str(database[record][1])) # Print data from that record.
            if str(database[record][4]) == "E": # Interpret status codes.
                print("Status: Estimate")
            elif str(database[record][4]) == "A":
                print("Status: Accepted Job")
            elif str(database[record][4]) == "N":
                print("Status: Not Accepted")
    if foundEstimate == False: # Warn the user if no record is found.
        print("Sorry. No estimate found for ID: " + str(estID))
    time.sleep(1)
    menu() # Callback to main menu

def displayOutstandingPayments(): # Declare function to print outstanding payments.
    global database # Initialise instance from database.
    totalOutstanding = 0 # Variable to hold the total outstanding.
    print("+---------------------------------------------------------------------+") # Table formatting.
    print("| {0} | {0} | {0} | {0} | {0} |". format("Estimate ID", "Customer ID",
    "Final Total", "Amount Paid", "Amount Outstanding"))
    print("+---------------------------------------------------------------------+")
    for record in range(0, len(database)): # For each record in the datbase
        if database[record][4] == "A" and database[record][3] != database[record][5]: # If it is accpted and not fully paid,
            totalOutstanding += (int(database[record][3]) - int(database[record][5])) # Add it to the totalOutstanding
            print("| {0:^11} | {1:^11} | {2:^11} | {3:^11} | {4:^11} |".format(
            database[record][0], database[record][2], database[record][3],
            database[record][5],
            str(int(database[record][3]) - int(database[record][5])))) # Print it's info.
    print("+---------------------------------------------------------------------+")
    print("| Total outstanding: " + str(totalOutstanding) + "                                             |") # In the end, print the totalOutstanding
    print("+---------------------------------------------------------------------+")
    time.sleep(1)
    menu() # Callback to main menu.

def displayTotalRevenue(): # declaration of function to display the total revenue.
    global database # Initialise database instance.
    totalRevenue = 0 # Variable to hold total revenue.
    for record in range(0, len(database)): # For each record in the database:
        if database[record][4] == "A" and int(database[record][3]) - int(database[record][5]) == 0: # If it si accepted and outstanding,
            totalRevenue += int(database[record][5]) # Add to the total.
    print("The company's total revenue is: £" + str(totalRevenue)) # In the end of going through all the records, print the total.
    time.sleep(1)
    menu() # Callback to main menu.

# MARK: Helper functions

def populateDatabase(): # Function to populate the database.
    with open("paintingJobs.txt", "r") as theFile: # Open the file,
        global database # Create databse instance.
        database = [] # Set it as a list.
        for line in theFile: # For each line,
            line = line.strip('\n') # Remove the ending.
            line = line.strip('\t')
            database.append(line.split(",")) #Add line to database

menu() # Start program.
