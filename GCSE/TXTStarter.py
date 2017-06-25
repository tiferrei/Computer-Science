#TXTStarter

#  Created by Tiago Ferreira on 22/02/2016.
#  Copyright (c) 2016 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import sys #import system module
data = input("Enter data: ") #inpput data to variable
with open("whatever.txt", mode="a", encoding="utf-8") as writeFile: #initialize file in append mode
    writeFile.write(data) #Append data
    writeFile.write("\n") #Append linebreak
while 1==1: #Loop for ever.
    askPrintData = input("Would you like to read all the data? (YES, NO): ") #Ask if the user wants to read the data.
    if askPrintData == "YES": #If yes:
        with open("whatever.txt", mode="r", encoding="utf-8") as readFile: ##initialize file in read mode
            for line in readFile: #for every line
                print(line.rstrip("\n")) #Print it without extra line
    else: #Else:
        askInputData = input(("Then would you like to add data? (YES, NO): ")) #Ask the user if he would like to append data.
        if askInputData == "YES": #If yes
            data = input("Enter data: ") #Ask for data
            with open("whatever.txt", mode="a", encoding="utf-8") as writeFile: #initialize fiel in append mode
                writeFile.write(data) #Write data
                writeFile.write("\n") #Add linebreak
        else: #Else
            print("Goodbye!") #goodbye
            sys.exit() #Exit
