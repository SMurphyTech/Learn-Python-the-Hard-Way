
# sets up a list called numbers
numbers = []
limit = 9

def loop(increment):
    
    for n in range(0, limit):
        # this code repeats in a loop if i is less than 6 
        print(f"At the top i is {n}")
        numbers.append(n)
    
        # every loop around, i increases by 1, so it'll eventually go higher than 6 and break the loop
        
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {n}")
        
loop(3)

# after the loop is broken, the rest of the code runs
print("The numbers: ")

for num in numbers:
    print(num)