from sys import argv

print("How old are you?", end=' ')
# saves what the user typed to a variable
age = input()
print("How tall are you?", end=' ')
# saves what the user typed to a variable
height = input()
print("How much do you weigh?", end=' ')
# saves what the user typed to a variable
weight = input()

# uses the entered variables to fill in a string
print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# adds another argument for you to enter when running the file from the command prompt
script, filename = argv

# opens the file entered
txt = open(filename)

print(f"Here's your file {filename}:")
# prints the contents of the file
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

# opens and reads file again
txt_again = open(file_again)

print(txt_again.read())

# a backslash before certain characters makes something else happen
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

# triple quote strings can go on for multiple lines
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")

# math
five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

# a function that takes an argument and uses it to define other variables
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    # returns a tuple
    return jelly_beans, jars, crates


start_point = 10000
# sets the value of a tuple to what the function returns
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cats = 30
dogs = 15

if people < cats:
    # 20 is less than 30, so this would print
    print("Too many cats! The world is doomed!")

if people > cats:
    # 20 is less than 30, so this wouldn't print
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    # since dogs equals 15 + 5, and people = 20, this would print
    print("People are dogs.")
