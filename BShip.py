
import random

vertical = []

horizontal1 = ["0  ", "0  ", "0  ", "0  ", "0  ", "0  "]
horizontal2 = ["0  ", "0  ", "0  ", "0  ", "0  ", "0  "]
horizontal3 = ["0  ", "0  ", "0  ", "0  ", "0  ", "0  "]
horizontal4 = ["0  ", "0  ", "0  ", "0  ", "0  ", "0  "]
horizontal5 = ["0  ", "0  ", "0  ", "0  ", "0  ", "0  "]
horizontal6 = ["0  ", "0  ", "0  ", "0  ", "0  ", "0  "]

vertical.append(horizontal1)
vertical.append(horizontal2)
vertical.append(horizontal3)
vertical.append(horizontal4)
vertical.append(horizontal5)
vertical.append(horizontal6)
    
boatX = []
boatY = []

boat1 = []
boat2 = []
boat3 = []
boat4 = []
boat5 = []

def print_grid():
    for y in vertical:
        for x in y:
            print(x, end = " ")
        print("\n")
        
def randomize_boats(how_many):
    for i in range(how_many):
        
        # determines if boat is horizontal or vertical
        direction = random.randint(1, 2)
        
        # vertical
        if(direction == 1):
            # determines length of the boat
            length = random.randint(1, 4)
            
            # determines where they show up on the board
            chance1 = random.randint(1, 6)
            chance2 = random.randint(1, 6)
            
            # starts with random coords, then extends the boat to random length
            for r in range(length):
                boatX.append(chance2)
                boatY.append(chance1)
                chance1 += 1
        
        # horizontal
        else:
            length = random.randint(1, 4)
            
            chance1 = random.randint(1, 6)
            chance2 = random.randint(1, 6)
            
            for r in range(length):
                boatY.append(chance1)
                boatX.append(chance2)
                chance2 += 1

randomize_boats(5)

print(boatX)
print(boatY)

print_grid()

def guess():    
    spotX = input("Enter an X coordinate:")
    spotY = input("Now a Y coordinate:")

    spotX = int(spotX)
    spotY = int(spotY)

    # to keep track of what index 'num' is at in boatX
    counter = 0

    for num in boatX:
        counter += 1
        print(counter)
    
        if spotX == num:
            if(spotY == boatY[counter - 1]):
                print("HIT!!")
                vertical[spotY - 1].pop(spotX - 1)
                vertical[spotY - 1].insert(spotX - 1, "X  ")
                break
            else:
                print("miss..")
                vertical[spotY - 1].pop(spotX - 1)
                vertical[spotY - 1].insert(spotX - 1, "-  ")
        else:
            print("miss..")
            vertical[spotY - 1].pop(spotX - 1)
            vertical[spotY - 1].insert(spotX - 1, "-  ")
        

    print_grid()
    
tries = 10

while(tries > 0):
    guess()
    tries -= 1
    