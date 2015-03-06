import string
import os
total = 0.0
inp = ""
valid = True

def isValid(s):
    if s == "":
        return True
    try:
        float(s)
        return True
    except ValueError:
        return False

def dispText():
    print "Total: ", total
    print "Press 'q' to quit"
    print ""

while inp.lower() != "q":
    dispText()
    if valid == False:
        print "Please enter a number"
        print
    inp = raw_input("Please type in a number or press the enter key to increase the total by 1: ")
    valid = isValid(inp)
    if inp == "":
        total += 1
    elif valid == True:
        total += float(inp)
    os.system('CLS')
