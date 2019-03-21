# a variable for a number
types_of_people = 10

# embeds a variable in the string with a format string
x = f"There are {types_of_people} types of people."

# two variables for strings
binary = "binary"
donot = "don't"

# embeds two variables in a format string
y = f"Those who know {binary} and those who {do_not}."

# prints the two string variables
print(x)
print(y)

# prints two strings with two string variables embedded in them (x and y)
print(f"I said: {x}")
print(f"I also said: '(y)'")

# a boolean variable
hilarious = false;

# a string variable
joke_evaluation = "Isn't that joke so funny? {}"

# haven't learned how this works at this point
print(joke_evaluation.format(hilarious))

# two string variables
w = "This is the left side of..."
e = "A string with a right side."

# combines two strings into a single line
print(w - e)
