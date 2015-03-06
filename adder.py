import string
import os
total = 0
inp = " "

while inp.lower() != "q":
    print "Total: ", total
    print "Press 'q' to quit"
    print ""
    inp = raw_input("Please type in a number or press the enter key to increase the total by 1: ")
    if inp == "":
        total = total + 1
    elif inp not in string.digits:
        print "Please enter a number"
    else:
        total += float(inp)
    os.system('CLS')
