#Function Challenge

#  Created by Tiago Ferreira on 08/02/2016.
#  Copyright (c) 2016 Tiago Ferreira. All rights reserved.

def Average():
    NumberOfNumbers = int(input("How many numbers do you want to calculate? "))
    NumArray = []
    for x in range(NumberOfNumbers):
        Number = float(input("Number: "))
        NumArray.append(Number)
    Total = 0
    for i in range(NumberOfNumbers):
        Total = Total + NumArray[(i-1)]
    Total = Total / NumberOfNumbers
    print("Your average is: "+ str(Total))

Average()
