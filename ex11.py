print("How old are you?", end = ' ')

#waits until the user types something in and presses enter and then assigns that string to a variable
age = input()

print("How tall are you?", end = ' ')

#waits until the user types something in and presses enter and then assigns that string to a variable
height = input()

print("How much do you weigh?", end = ' ')

#waits until the user types something in and presses enter and then assigns that string to a variable
weight = input()

#fills in the variables with the user input
print(f"So, you're {age} old, {height} tall and {weight} heavy.")

print("What is your name?")
name = input()
print("What is your pet's name?")
petName = input()
print("What kind of things do you give your pet?")
give = input()

print(f"{name} gives {give} to their pet, {petName}.")