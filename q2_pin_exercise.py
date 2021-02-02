# Question 2 - pin number exercise
# There are 2 versions for question 2 and one for question 3 here
# Comment out any section you don't want to test to avoid confusion

# The code below works and uses if statement in a flow-chart style

pin = "1234"
supplied_pin = input("Enter your pin: ")
if supplied_pin == pin:
    print("Pin Accepted")
else:
    print("Pin Incorrect. 2 Tries Left")
    supplied_pin = input("Enter your pin: ")
    if supplied_pin == pin:
        print("Pin Accepted")
    else:
        print("Pin Incorrect. 1 Try Left")
        supplied_pin = input("Enter your pin. Last Try: ")
        if supplied_pin == pin:
            print("Pin Accepted")
        else:
            print("Pin Incorrect. No more Tries")


# The code below also works for question 2 but is shorter and uses the 'while' command and therefore probably preferred

pin = "1234"
attempts = 1
supplied_pin = input("Enter your pin: ")

while attempts < 4:
    if supplied_pin == pin:
        print("Pin Accepted")
        break
    else:
        print("Pin Incorrect.", 3 - attempts, "Attempt(s) Remaining")
        attempts += 1
        if attempts < 4:
            supplied_pin = input("Enter your pin: ")


#Question 3 - tried to use getpass.getpass in the way it says but this doesn't work for me!

import getpass
import sys


attempts = 1
supplied_pin = getpass.getpass("Enter Your Pin Number: ")

while attempts < 4:
    if supplied_pin == 1234:
        print("Pin Accepted")
        break
    else:
        print("Pin Incorrect.", 3 - attempts, "Attempt(s) Remaining")
        attempts += 1
        if attempts < 4:
            supplied_pin = getpass.getpass("Enter Your Pin Number: ")