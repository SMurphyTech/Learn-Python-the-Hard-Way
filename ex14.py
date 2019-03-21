#adds the argv variable from sys
from sys import argv

#prompts the user for the name of the file and their own name in the bash console
script, user_name, age = argv
prompt = 'Enter: '

#prints with variables from user input
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")

print(f"You're {age} years old, aren't you?")

if(int(age) > 18):
    print("Where do you work?")
    workplace = input(prompt)
elif(int(age) <= 18):
    print("Where do you go to school?")
    school = input(prompt)

#prompts the user for more input
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

#prints out all the previously entered variables
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")