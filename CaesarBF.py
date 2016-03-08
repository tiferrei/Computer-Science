#Caesar Brute Forcer

#  Created by Tiago Ferreira and Alex Butler on 2/03/2016.
#  Copyright (c) 2016 Tiago Ferreira and Alex Butler. All rights reserved.

import time, sys, csv, os

Letters = ["A", "B", "C", "D", "E", "F",
            "G", "H", "I", "J", "K", "L",
            "M", "N", "O", "P", "Q", "R",
            "S", "T", "U", "V", "W", "X",
            "Y", "Z"]
message = input("Message to brute force: ")
message = message.upper()
messageEncrypted = message
message = message.split(" ")
messageAdd = []
messageAdded = ""
decryptedMessage = ""
decryptedAttemptWord = ""
foundDecryptedMessage = False
failedAttemptRecord = {}

with open("dictionary.csv") as csvfile:
    dictionaryCSV = csv.reader(csvfile, delimiter="\n")
    words = []
    for row in dictionaryCSV:
        word = row[0]
        words.append(word)

for n in range(len(message)):
    for i in range(1,26):
        looper = i
        for x in range(len(message[n])):
            letter = message[n]
            letter = letter[x]
            letter = letter.upper()
            if letter != " ":
                currentLetter = Letters.index(letter)
                newLetter = currentLetter + (looper - 1)
                if newLetter > 25:
                    newLetter = newLetter - 26
                decryptedLetter = Letters[newLetter]
                decryptedMessage = decryptedMessage + decryptedLetter
            else:
                letter = message[x+1]
                letter = letter.upper()
                decryptedMessage = decryptedMessage + " "
        if decryptedMessage in(words):
            # print('Decrypted message: "' + decryptedMessage + '" on ROT' + str(i-1))
            messageAdd.append(decryptedMessage)
            foundDecryptedMessage = True
        else:
            FailedAttemptROT = i
            FailedAttemptMessage = decryptedMessage
            failedAttemptRecord[FailedAttemptROT] = FailedAttemptMessage
            decryptedMessage = ""
for items in range(len(messageAdd)):
    messageAdded = messageAdded + messageAdd[items] + " "
messageAdded = messageAdded[:-1]
if foundDecryptedMessage == True:
            print('Decrypted message: "' + messageAdded + '" on ROT' + str(i-2))
elif foundDecryptedMessage == False:
    print("No correct english frase/word identified.")
    time.sleep(0.5)
    messageIsCorrect = input('Is the encrypted message, "' + messageEncrypted + '" correct? (YES, NO): ')
    time.sleep(0.5)
    if messageIsCorrect == "YES":
        print("OK, so I'll give you all the possibilites...")
        print()
        for y in range(1,26):
            time.sleep(0.3)
            print('ROT' + str(y-1) + " -> " + failedAttemptRecord[y])
        correctAttemptIsAvailable = input("Was there any correct attempt? (YES, NO): ")
        if correctAttemptIsAvailable == "YES":
            AttemptChosenIsRight = False
            while AttemptChosenIsRight == False:
                correctAttempt = 1 + int(input("According to the rotations, which one was it? (1, 2, 3, etc.): "))
                correctAttemptChosen = failedAttemptRecord[correctAttempt]
                correctAttemptIsRight = input('"' + correctAttemptChosen + '", this one? (YES, NO): ')
                if correctAttemptIsRight == "YES":
                    AttemptChosenIsRight = True
                    print("Thanks, I'll add the new words to the dictionary.")
                    for z in range(len(failedAttemptRecord[correctAttempt])):
                        decryptedAttempt = failedAttemptRecord[correctAttempt]
                        decryptedAttemptLetter = decryptedAttempt[z]
                        decryptedAttemptLetter = decryptedAttemptLetter.upper()
                        if decryptedAttemptLetter != " ":
                            decryptedAttemptWord = decryptedAttemptWord + decryptedAttemptLetter
                        else:
                            with open('dictionary.csv', 'a', newline='') as csvfile:
                                DictWrite = csv.writer(csvfile, delimiter=',')
                                DictWrite.writerow([decryptedAttemptWord])
                            decryptedAttemptWord = ""
        else:
            print("Then you got some typo mistake, restarting...")
            time.sleep(0.5)
            os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        print("Restarting...")
        time.sleep(0.5)
        os.execl(sys.executable, sys.executable, *sys.argv)
