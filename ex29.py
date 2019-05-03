people = 20
cats = 30
dogs = 15

if people < cats:
    # 20 is lesser than 30, so this would run
    print("Too many cats! The world is doomed!")
    
if people > cats:
    # 20 is lesser than 30, so this wouldn't run
    print("Not many cats! The world is saved!")
    
if people < dogs:
    # 20 is greater than 15, so this wouldn't run
    print("The world is drooled on!")
    
if people > dogs:
    # 20 is greater than 15, so this would run
    print("The world is dry!")
    
    
dogs += 5

if people >= dogs:
    # 20 is equal to 20, so this would run
    print("People are greater than or equal to dogs.")
    
if people <= dogs:
    # 20 is equal to 20, so this would run
    print("People are less than or equal to dogs.")
    
if people == dogs:
   # 20 is equal to 20, so this would run
    print("People are dogs.")