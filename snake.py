wall = "X"
x = 4
y = 5

prompt = '> '
print("What map do you want to play on?")
file = input(prompt)

map = open(file, 'r+')
lines = map.readlines()

def printMap():
    i = 0
    for line in lines:
        print(lines[i])
        if(i == y):
            print("X" + " " * x + "0")
        i = i + 1

printMap()

while(True):
    print("Which direction? N/S/E/W")
    direction = input()

    if(direction == 'N' or direction == 'n'):
        y = y - 1
        print(x, y)
    if(direction == 'S' or direction == 's'):
        y = y + 1
        print(x, y)
    if(direction == 'W' or direction == 'w'):
        x = x - 3
        print(x, y)
    if(direction == 'E' or direction == 'e'):
        x = x + 3
        print(x, y)

    printMap()
