# defines a function that takes two arguments
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# does the same thing as function #1, but with less code
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# defines a function that takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# defines a function that takes no arguments
def print_none():
    print("I got nothin'.")

# functions are called with arguments
print_two("Sean", "Murphy")
print_two_again("Rainbow", "Curse")
print_one("First!")
print_none()
