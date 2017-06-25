#Summing Starter

#  Created by Tiago Ferreira on 01/02/2016.
#  Copyright (c) 2016 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import random, sys #Import some modules

def summing(): #Define Summing
    GotItSumming = 0 #Initialize variable
    for x in range(1,6): #Loop for 5 times
        Number1 = random.randint(100, 500) #Generate random int
        Number2 = random.randint(100, 500) #Generate random int
        UserAnswer = int(input("What's the sum of " + str(Number1) + " and " + str(Number2) + "? ")) #Ask question
        Total = Number1 + Number2 #Get correct answer

        if UserAnswer == Total: #If the answer is correct:
            print("Well Done!") #Well done
            GotItSumming = GotItSumming + 1 #Add 1 point
        else: #Else:
            print("Wrong, the answer was " + str(Total)) #Give correct answer
    print("you got " + str(GotItSumming) + " questions right!") #At the end, say the number of correct answers

def subtracting(): #Define subtracting
    GotItSubtracting = 0 #Initialize variable
    for x in range(1,6): #Loop for 5 times
        Number1 = random.randint(100, 500) #Generate random int
        Number2 = random.randint(100, 500) #Generate random int
        UserAnswer = int(input("What's the subtraction of " + str(Number1) + " and " + str(Number2) + "? ")) #Ask question
        Total = Number1 - Number2 #Get correct answer

        if UserAnswer == Total: #If the answer is correct:
            print("Well Done!") #Well done
            GotItSubtracting= GotItSubtracting + 1 #Add 1 point
        else: #Else:
            print("Wrong, the answer was " + str(Total)) #Give correct answer
    print("you got " + str(GotItSubtracting) + " questions right!") #At the end, say the number of correct answers

def multiplying(): #Define multiplying
    GotItMutliplying = 0 #Initialize varible
    for x in range(1,6): #Loop for 5 times
        Number1 = random.randint(2, 12) #Generate random number
        Number2 = random.randint(2, 12) #Generate random number
        UserAnswer = int(input("What's the multiplication of " + str(Number1) + " and " + str(Number2) + "? ")) #Ask question
        Total = Number1 * Number2 #Calculate correct answer

        if UserAnswer == Total: #
            print("Well Done!")
            GotItMutliplying = GotItMutliplying + 1
        else:
            print("Wrong, the answer was " + str(Total))
    print("you got " + str(GotItMutliplying) + " questions right!")

def dividing(): #Define multiplying
    GotItDividing = 0 #Initialize varible
    for x in range(1,6): #Loop for 5 times
        Number1 = random.randint(2, 12) #Generate random number
        Number2 = random.randint(2, 12) #Generate random number
        UserAnswer = int(input("What's the devision of " + str(Number1) + " and " + str(Number2) + "? ")) #Ask question
        Total = Number1 / Number2 #Calculate correct answer

        if UserAnswer == Total: #
            print("Well Done!")
            GotItDividing = GotItDividing + 1
        else:
            print("Wrong, the answer was " + str(Total))
    print("you got " + str(GotItDividing) + " questions right!")

def Quiz():
    while 1 == 1:
        IsValid = False
        while IsValid == False:
            print()
            print("""What do you want to do?
            A -> Addition Quiz
            B -> Multiplication Quiz
            C -> Subtraction Quiz
            D -> Dividing Quiz
            Q -> Quit""")

            UserChoice = input("(A, B, C, D or Q): ")

            if UserChoice == "Q":
                IsValid = True
                sys.exit()
            elif UserChoice == "A":
                IsValid = True
                summing()
            elif UserChoice == "B":
                IsValid = True
                multiplying()
            elif UserChoice == "C":
                subtracting()
                IsValid = True
            elif UserChoice == "D":
                dividing()
                IsValid = True
            else:
                print("Ivalid, please enter A, B, C, D or Q")
                IsValid = False

Quiz()
