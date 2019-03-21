from sys import argv

#expects two arguments before running the program
scirpt, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# hitting control-c creates an error and stops the run of the program, hitting enter just continues the run
input("?")

print("Opening the file...")

#file is opened
target = open(filename, 'w')

#contents of the file was erased
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

#user enters three lines
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

#writes the three entered lines into the txt file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
#file is closed
target.close()