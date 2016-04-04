#Username And Password

#  Created by Tiago Ferreira on 25/11/2015.
#  Copyright (c) 2015 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import time #import time module.
import sys #import sys module.

upercaseOptions = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", #create list for upercase options.
                   "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numberOptions = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] #create list for numeral options.

specialCharOptions = ["!","@", "[", "]", "#", "€", "", "£", "$", "%", "^", "&", #Create list for special characters options.
                      "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "]", "~",
                      "#", ":", ";", "'", "/", "|"]


passwordIsntValid = True #Close the loop
validLenght = False #Set the chekcs to faulse by default.
validNumber = False #Set the chekcs to faulse by default.
validSpecialChar = False #Set the chekcs to faulse by default.
validUperCase = False #Set the chekcs to faulse by default.

username = input("Username: ") #Put the username in a variable.

while passwordIsntValid == True: #Start while loop.

    password = input("Password: ") #Put the password in a variable.

    print("Checking values...") #Give info to the user.
    time.sleep(0.5) #Wait half a second.

    if len(password) > 7: #Check for the length of the password.
        validLenght = True #If yes, set the variable as true.




    for character in password: #For loop to do the instructions for every character.
        if character in upercaseOptions: #If the character is in uperOptions,
            validUperCase = True #Set Uper case check as true.
        if character in numberOptions: #If the character is in numberOptions,
            validNumber = True #Set number check as true.
        if character in specialCharOptions: #If the character is in specialCharOptions,
            validSpecialChar = True #Set special check as true.


    if validLenght == True and validSpecialChar == True and validNumber == True and validUperCase == True: #If all the checks are truem

        print("Your password is valid.") #Tell the user that the password is valid.

        checkPasswordIsntValid = True #Close the loop.

        while checkPasswordIsntValid == True: #Start the loop.

            checkPassword = input("Please retype your password: ") #Put the password to check in a variable.

            if password == checkPassword: #If the passwords match,
                print("Passwords match.") #Tell the user,
                time.sleep(0.5) #Wait half a second,
                print("Password saved.") #Tell that the password was saved.
                print("Username: " + username) #Print the username.
                print("Password: " + password) #Print the password.
                time.sleep(0.5) #Wait half a second.
                sys.exit() #Exit the program.
            else: #Else,
                print("Passwords don't match, please try again.") #Print that the passwords don't match
                time.sleep(0.3) #Wait 0.3 seconds.
    else: #Else,
        print("""Your password must have at least 8 characters, 1 number, 1 upper
case letter and a special character. Please try again.""") #Help the user.
        time.sleep(0.5) #Wait half a second.
        sys.exit() #Exit the program.
