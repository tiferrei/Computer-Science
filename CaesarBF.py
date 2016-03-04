#Caesar Brute Forcer

#  Created by Tiago Ferreira and Alex Butler on 2/03/2016.
#  Copyright (c) 2016 Tiago Ferreira and Alex Butler. All rights reserved.

import time
import sys
import csv

Letters = ["A", "B", "C", "D", "E", "F",
            "G", "H", "I", "J", "K", "L",
            "M", "N", "O", "P", "Q", "R",
            "S", "T", "U", "V", "W", "X",
            "Y", "Z"]
message = input("Message to brute force: ")
message = message.upper()
decryptedMessage = ""
decryptedAttemptWord = ""
FailedAttemptRecord = {}

with open("dictionary.csv") as csvfile:
    dictionaryCSV = csv.reader(csvfile, delimiter="\n")
    words = []
    for row in dictionaryCSV:
        word = row[0]
        words.append(word)

for i in range(1,26):
    looper = i
    for x in range(len(message)):
        letter = message[x]
        letter = letter.upper()
        currentLetter = Letters.index(letter)
        newLetter = currentLetter + (looper - 1)
        if newLetter > 25:
            newLetter = newLetter - 26
        decryptedLetter = Letters[newLetter]
        decryptedMessage = decryptedMessage + decryptedLetter
    if decryptedMessage in(words):
        print('Decrypted message: "' + decryptedMessage + '" on ROT' + str(i-1))
    else:
        FailedAttemptROT = i
        FailedAttemptMessage = decryptedMessage
        FailedAttemptRecord[FailedAttemptROT] = FailedAttemptMessage
        decryptedMessage = ""

print("No correct english frase/word identified. ")
messageIsCorrect = input('Is the encrypted message, "' + message + '" correct? (YES, NO): ')
time.sleep(0.5)
if messageIsCorrect == "YES":
    print("OK, so I'll give you all the possibilites...")
    print()
    for y in range(1,26):
        time.sleep(0.3)
        print('ROT' + str(y-1) + " -> " + FailedAttemptRecord[y])
    correctAttemptIsAvailable = input("Was there any correct attempt? (YES, NO): ")
    if correctAttemptIsAvailable == "YES":
        correctAttempt = 1 + int(input("According to the rotations, which one was it? (1, 2, 3, etc.): "))
        correctAttemptChosen = FailedAttemptRecord[correctAttempt]
        correctAttemptIsRight = input('"' + correctAttemptChosen + '", this one? (YES, NO): ')
        if correctAttemptIsRight == "YES":
            print("Thanks, I'll add the new words to the dictionary.")
            for z in range(len(FailedAttemptRecord[correctAttempt])):
                decryptedAttempt = FailedAttemptRecord[correctAttempt]
                decryptedAttemptLetter = decryptedAttempt[z]
                decryptedAttemptLetter = decryptedAttemptLetter.upper()
                if decryptedAttemptLetter != " ":
                    decryptedAttemptWord = decryptedAttemptWord + decryptedAttemptLetter
            print("This would add:" + decryptedAttemptWord)
            #Replace the previous print with your code, thanks.
