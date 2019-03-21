from sys import argv

#expects 2 arguments
script, input_file = argv

#defines functions used later
#prints all lines in a file
def print_all(f):
    print(f.read())

#goes back to the first line
def rewind(f):
    f.seek(0)

#takes a number as an argument, and then prints the line at that number
def print_a_line(line_count, f):
    print(line_count, f.readline())

#opens the file
current_file = open(input_file)

print("First let's print the whole file:\n")

#prints the entire file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

#goes back to the first line
rewind(current_file)

print("Let's print three lines:")

#prints the first, second, and third line in the file
while(current_line < 3):
    print_a_line(current_line, current_file)
    current_line += 1
