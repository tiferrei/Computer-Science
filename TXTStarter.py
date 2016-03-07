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
