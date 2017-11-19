#  Customer Loyalty Scheme

#  Created by Tiago Ferreira on 18/10/2017.
#  Copyright (c) 2017 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

from datetime import date
from random import randint

# MARK: Helper Tools

class Member():
    def __init__(self, ID, surname, yearJoined, membershipStatus, nightsBooked, pointsBalance):
        self.surname = str(surname)
        self.yearJoined = int(yearJoined)
        self.membershipStatus = str(membershipStatus)
        self.nightsBooked = int(nightsBooked)
        self.pointsBalance = int(pointsBalance)
        self.ID = str(ID)

    def generateNewID(self):
        self.ID = self.surname[:3] + str(randint(100, 999)) + str(self.yearJoined)[-2:]

    def updateRank(self):
        if self.nightsBooked < 30:
            self.membershipStatus = "Silver"
        elif self.nightsBooked >= 30 and self.nightsBooked < 100:
            self.membershipStatus = "Gold"
        elif self.nightsBooked >= 100:
            self.membershipStatus = "Platinum"

    def addStay(self, numberOfNights):
        if self.pointsBalance // 25000 > numberOfNights:
            self.pointsBalance -= numberOfNights * 25000
        else:
            self.pointsBalance -= (self.pointsBalance // 25000) * 25000
        if self.membershipStatus == "Silver":
            self.pointsBalance += 2500 * numberOfNights
        elif self.membershipStatus == "Gold":
            self.pointsBalance += 3000 * numberOfNights
        elif self.membershipStatus == "Platinum":
            self.pointsBalance += 4000 * numberOfNights
        self.nightsBooked += numberOfNights
        self.updateRank()

class DB():
    def __init__(self):
        self.members = []
        with open("SampleData2017.txt", "r") as file:
            for rawLine in file:
                line = rawLine.split(",")
                dbMember = Member(line[0], line[1], line[2], line[3], line[4], line[5])
                self.members.append(dbMember)

    def saveDB(self):
        print(self.members)
        with open("SampleData2017.txt", "w") as file:
            for member in self.members:
                file.write(member.ID + "," + member.surname + ",")
                file.write(str(member.yearJoined) + "," + member.membershipStatus)
                file.write("," + str(member.nightsBooked) + "," + str(member.pointsBalance) + "\n")

    def addMember(self, newMember):
        self.members.append(newMember)
        with open("SampleData2017.txt", "a") as file:
            file.write(newMember.ID + "," + newMember.surname + ",")
            file.write(str(newMember.yearJoined) + "," + newMember.membershipStatus)
            file.write("," + str(newMember.nightsBooked) + "," + str(newMember.pointsBalance) + "\n")

# MARK: Subroutines

def memberEnrollement(database):
    print("Please enter the following information:")
    newMember = Member(0, input("Surname: ").split(" ")[0], date.today().year + 1, "Silver", 0, 0)
    newMember.generateNewID()
    database.addMember(newMember)

def bookStay(database):
    memberID = input("Please enter member ID: ")
    foundMember = False
    for member in database.members:
        if member.ID == memberID:
            foundMember = True
            member.addStay(int(input("Please enter the number of days to stay: ")))
            database.saveDB()
    if foundMember == False:
        print("Member not found, register member or search for correct ID in the Database.")
        menu()

def printDB(database):
    for member in database.members:
        print("Information for Member ID: " + member.ID)
        print("    Surname: " + member.surname)
        print("    Year Joined: " + str(member.yearJoined))
        print("    Membership Status: " + member.membershipStatus)
        print("    Nights Booked: " + str(member.nightsBooked))
        print("    Points Balance: " + str(member.pointsBalance))
        print()

# MARK: Main

def main():
    database = DB()

    print("Welcome, please select an option:")
    print("1: Enroll new member")
    print("2: Book stay")
    print("3: Display Database")
    selection = int(input("Enter selection: "))

    while selection not in range(1,4):
        print("Invalid Input. Enter 1, 2 or 3.")
        selection = int(input("Enter selection: "))

    if selection == 1:
        memberEnrollement(database)
    elif selection == 2:
        bookStay(database)
    elif selection == 3:
        printDB(database)

main()
