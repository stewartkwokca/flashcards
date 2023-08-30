import os
from random import randint

# Copies a 2D array
def copyTwoDimArr(arr):
    newArr = []
    for i in range(len(arr)):
        row = []
        for j in range(len(arr[i])):
            row.append(arr[i][j])
        newArr.append(row)
    return newArr

# Study
def study(cards):
    allCardsList = []
    notStudied = []

    for line in cards:
        allCardsList.append(line.strip().split(":"))
        notStudied.append(line.strip().split(":"))

    ctr = 0
    ctrWrong = 0
    x = len(allCardsList)

    # Studying loop
    studying = True
    while studying:
        terms = len(notStudied)
        if terms > 0:
            i = randint(1, terms) - 1
            print("TERM: " + notStudied[i][0])
            ans = input("DEFINITION: ")
            correctDef = notStudied[i][1]
            if ans != correctDef:
                ctrWrong += 1
                print("INCORRECT.")
                print("ANSWER WAS: " + correctDef)
            else:
                ctr += 1
                print("CORRECT!")
                notStudied.remove(notStudied[i])

            print(str(ctr) + "/" + str(x) + " terms studied")
            print("Incorrect: " + str(ctrWrong))
                
        else:
            ctr = 0
            print("YOU'VE STUDIED ALL YOUR TERMS!")
            print("Incorrect: " + str(ctrWrong))
            ctrWrong = 0
            q = input("ENTER Q to QUIT or ANYTHING ELSE to PRACTICE AGAIN: ").upper()
            if q != "Q":
                notStudied = copyTwoDimArr(allCardsList)
            else:
                studying = False
        print("************************")
