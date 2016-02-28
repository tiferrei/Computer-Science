#Darren Recursive Functions

#  Created by Tiago Ferreira on 28/02/2016.
#  Copyright (c) 2016 Darren Bianchini. All rights reserved.

# Stack Overflow when passing number 998.

def sumUpTo(n):
    if n > 1:
        total = sumUpTo(n-1) + n
    else:
        total = 1
    return total

n = int(input("Give me a number (23): "))
print(sumUpTo(n))
