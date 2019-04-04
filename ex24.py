
# you can add ' without ending the string by adding a backslash before it
# you can only add a backslash toa string by typing 2 backslash
# \n adds a newline and \t adds a tab
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

# triple quotes allow a string to span multiple lines
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
#prints the previously defined variable poem
print("-------------")
print(poem)
print("-------------")

# the equation comes out to 5, setting the variable five to 5
five = 10 - 2 + 3 - 6
#prints the five variable in a format string
print(f"This should be five: {five}")

#defines a function that takes one argument, started
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
    


start_point = 10000
# runs the secret_formula function and sets the tuple it returns to another tuple
beans, jars, crates = secret_formula(start_point)

# a different way of doing a format string
print("With a starting point of: {}".format(start_point))
# another format string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
#sets the tuple secret_formula returns to the variable formula

word = "floss"
formula = secret_formula(word)

# applies a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))