#imports the argv variable
from sys import argv

#declares that two arguments are expected to be entered
script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

txt.close()

#prompts the user to enter the filename again
print("Type the filename again:")
file_again = input("> ")

#opens and prints the filename entered
txt_again = open(file_again)
print(txt_again.read())

txt_again.close()