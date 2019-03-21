# imports the needed module so that python knows what
# to do with 'argv'
from sys import argv

# read the WYSS section fro how to run this
# asigns the arguments typed in the bash console to variables
script, first = argv

second = input("You entered " + first + ". Would you like to enter something else? ")

print("You entered " + first + " and " + second + ".")