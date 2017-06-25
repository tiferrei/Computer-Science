#script to check contents of a variable
def stringtest(): #Define function
    user_input = input("Please enter a string of text between 8 and 16 characters long: ") #Get user string.
    user_letter = input("Please enter a letter of the alphabet (capital or lower case): ") #Get user letter.
    #Question 1
    while len(user_input) < 8 or len(user_input) > 16: #While length not between 8 and 16.
        print("The entered string is not between 8 and 16 characters") #Say the string is invalid.
        print("Your string is",len(user_input),"characters long") #Print the actual length.
        user_input = input("Please enter a new string: ") #Ask for a new string.
    print("\n") #Print blank line.

    #Question 2
    if user_letter in user_input: #If the letter is present in the string:
        print("The entered letter is present in your string of text \n") #Say that it is.
    else: #Else:
        print("The entered letter is NOT present in your string of text \n") #Say that it isn't.

    #Question 3
    if user_input.isalpha()==1: #If the string is composed of letters only:
        print("Your string contains only letters \n") #Say that it is.
    else: #Else:
        print("Your string may contain non alphabetical characters \n") #Say that it isn't.

    #Question 4
    if user_input.isdigit()==1: #If the string is composed of numbers only:
        print("Your string contains only numbers \n") #Say that it is.
    else: #Else:
        print("Your string contains non numerical characters \n") #Say that it isn't.

    #Question 5
    if user_input.isalnum()==1: #If the string is composed of letters and numbers only:
        print("Your string contains alphnumeric characters only \n") #Say it is.
    else: #Else:
        print("Your string contains non-alphanumeric characters \n") #Say it isn't.

    #Question 6
    if user_input.isupper()==1: #If the string is composed of uppercase leters only:
        print("Your string contains only uppercase characters \n") #Say it is.
    else: #Else:
        print("Your string contains some lowercase characters \n") #Say it isn't.

    #Question 7
    upper_present = False #Make variable false.
    for letter in user_input: #Start loop for every letter of variable.
        if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": #If the letter is in the uppercase alphabet:
            upper_present = True #Set the variable as true.
            break #Break the loop.
    if upper_present==True: #If the variable is true:
        print("Your string contains at least one uppercase letter \n") #Say it contains at least one uppercase letter.
    else: #Else:
        print("Your string contains no uppercase letters \n") #Say it doesn't.

    #Question 8
    if user_input.islower()==1: #Check if the string is composed of lowercase characters only:
        print("Your string contains only lowercase characters \n") #Say it is.
    else: #Else:
        print("Your string contains some uppercase characters \n") #Say it isn't.

    #Question 9
    lower_present = False #Create variable and set to false.
    for letter in user_input: #Loop for each letter of the string.
        if letter in "abcdefghijuklmnopqrstuvwxyz": #If the letter is in the lowercase alphabet:
            lower_present = True #Set the variable as true.
            break #Break the loop.
    if lower_present==True: #If the variable is true:
        print("Your string contains at least one lowercase letter \n") #Say that the string contains at least one lowercase letter.
    else: #Else:
        print("Your string contains no lowercase letters \n") #Say that the string contains no lowercase letters.


stringtest(); #Execute the function.
