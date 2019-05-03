
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
  
boat1X = []
boat1Y = []
boat2X = []
boat2Y = []
boat3X = []
boat3Y = []
boat4X = []
boat4Y = []
boat5 = []  
    
boatX = [boat1X, boat2X, boat3X, boat4X]
boatY = [boat1Y, boat2Y, boat3Y, boat4Y]

boatCount = 0
repeat = False

def print_grid():
    for y in vertical:
        for x in y:
            print(x, end = " ")
        print("\n")
        

def check_repeats(choiceX, choiceY):
    #print("choiceX = " + str(choiceX))
    #print("choiceY = " + str(choiceY))
    for boat in boatX:
        boat2 = boatY[boatX.index(boat)]
        for block in boat:
            #print("block = " + str(block))
            
            respectiveY = boat2[boat.index(block)]
            if choiceX == block:
                #print("X's match up")
                
                #print("lastY = " + str(respectiveY))
                if choiceY == respectiveY:
                    print("repeat!") 
                    
                    repeat = True


def randomize_boats(how_many):
    count = 0
    
    for i in range(how_many):
        
        # determines if boat is horizontal or vertical
        direction = random.randint(1, 2)
        
        # vertical
        if(direction == 1):
            print("vertical")
            # determines length of the boat
            length = random.randint(1, 4)
            
            # determines where they show up on the board
            chance1 = random.randint(1, 6)
            chance2 = random.randint(1, 6)
            
            # starts with random coords, then extends the boat to random length
            for r in range(length):
                check_repeats(chance2, chance1)
                if(repeat == True):
                    break
                boatX[count].append(chance2)
                boatY[count].append(chance1)
                chance1 += 1
        
        # horizontal
        else:
            print("horizontal")
            length = random.randint(1, 4)
            
            chance1 = random.randint(1, 6)
            chance2 = random.randint(1, 6)
            
            for r in range(length):
                check_repeats(chance2, chance1)
                if(repeat == True):
                    break
                boatX[count].append(chance2)
                boatY[count].append(chance1)
                chance2 += 1
        
        count += 1
        #print(count)

randomize_boats(4)

print(boatX)
print(boatY)

print_grid()

def guess():    
    spotX = input("Enter an X coordinate:")
    spotY = input("Now a Y coordinate:")

    spotX = int(spotX)
    spotY = int(spotY)

    # to keep track of what index 'num' is at in boatX
    count1 = 0
    count2 = 0
    
    hit = False

    for boat in boatX:
        
        if(hit == True):
            break
        
        count1 += 1
        print(count1)
        print(boat)
        
        yboat = boatY[count1 - 1]
        
        print(yboat)
        
        count2 = 0
        
        for block in boat:
            count2 += 1
            print(count2 - 1)
            
            if spotX == block:
                if(spotY == yboat[count2 - 1]):
                    print("HIT!!")
                    hit = True
                    vertical[spotY - 1].pop(spotX - 1)
                    vertical[spotY - 1].insert(spotX - 1, "X  ")
                    boat.pop(count2 - 1)
                    yboat.pop(count2 - 1)
                    
                    if(len(boat) == 0 and len(yboat) == 0):
                        print("Boat destroyed!")
                        #boatCount += 1
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
    