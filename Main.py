import os
import FlashcardsLibrary

# Directory of Folder
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Intro
print("Hello. Welcome to the digital flashcard program.")
print("************************")
print("Enter one of the following:")
print("C to CREATE SET")
print("S to STUDY SET")
action = input().upper()
print("************************")

if action == "S":
    setName = input("Enter set name: ") + ".txt"
    txtLoc = os.path.join(__location__, setName)
    while not os.path.exists(txtLoc):
        print("Set not found!")
        setName = input("Enter set name: ") + ".txt"
        txtLoc = os.path.join(__location__, setName)
    # Open Set
    cards = open(txtLoc) # Default value is read only
    FlashcardsLibrary.study(cards)
    cards.close()
if action == "C":
    print("If you make any mistakes, just correct them in the text file later.")
    setName = input("Enter set name: ") + ".txt"
    txtLoc = os.path.join(__location__, setName)
    cards = 0
    try:
        cards = open(txtLoc, "x")
    except:
        print("Set already exists!")
    q = ""
    if cards == 0:
        q = "Q"
    while q != "Q":
        term = input("Enter your term: ")
        definition = input("Enter your definition: ")
        line = term + ":" + definition + "\n"
        cards.write(line)
        q = input("Enter Q to QUIT, any other key to continue: ").upper()
    if cards != 0:
        cards.close()
else:
    print("BRO GONNA BE HONEST IDK WHAT U WANT ME TO DO")
