import time
import random

story = True
test = True
item = "nothing"
y = 0

class Item:
    index = 0

class Weapon(Item):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Restorative(Item):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

BBoom = Weapon("Bladed Boomerang", 40)
PP = Restorative("Pink Potion", 10)

equipped = BBoom

if test == True:
    print(equipped.damage)
    print(PP.hp)

# current inventory (item : quantity)
inventory = {
     BBoom : 1,
     PP : 3
}

# prints out inventory and quantities
def checkPack():
    for i in inventory:
        quantity = inventory[i]
        print(i.name + " x" + str(quantity))

# dictionary of all monsters (name : health)
monsterDict = {
    "Gelaton": 200
}

def battleInit(monster):
    monsterHealth = monsterDict[monster]
    num = 0

    while monsterHealth > 0:
        time.sleep(1)
        print("What will you do now?")
        action = input()
        if action == "attack" or action == "hit" or action == "strike":
            print("You swung at the " + monster + "!")
            time.sleep(1)
            chance = random.randint(1, 6)
            damage = random.randint(45, 49)

            if chance == 5:
                for m in "A Critical Hit!":
                    print(" " * num + m)
                    num = num + 1
                time.sleep(.5)
                damage = damage * 2
                print("You struck the " + monster + " for " + str(damage) + " damage!")
                monsterHealth = monsterHealth - damage
                if(monsterHealth > 0):
                    print("The " + monster + " has " + str(monsterHealth) + " health left!")
                else:
                    if story == True:
                        time.sleep(.5)
                        print("The " + monster + "'s health goes below 0...")
                        time.sleep(.5)
                        print("But the " + monster + " didn't die?")
                    else:
                        time.sleep(.5)
                        print("The " + monster + " is slain!!")
                        time.sleep(.5)
                        print("You collected 'gold' and 'exp'.")
            else:
                print("You struck the " + monster + " for " + str(damage) + " damage!")
                monsterHealth = monsterHealth - damage
                if(monsterHealth > 0):
                    print("The " + monster + " has " + str(monsterHealth) + " health left!")
                else:
                    if story == True:
                        time.sleep(.5)
                        print("The " + monster + "'s health goes below 0...")
                        time.sleep(.5)
                        print("But the " + monster + " didn't die?")
                    else:
                        time.sleep(.5)
                        print("The " + monster + " is slain!!")
                        time.sleep(.5)
                        print("You collected 'gold' and 'exp'.")
        elif item == "crumpled up piece of paper." and action == "read paper" or item == "crumpled up piece of paper." and action == "read":
            print("You unfold and read the piece of paper. It's a badly drawn picture of a banana. I don't know what it means either.")
        elif action == "die":
            monsterHealth = monsterHealth - 50000
        else:
            print("That won't work...")
    else:



#scroll("Tester")

time.sleep(1)
print("A gelatinous monster seeps out of nowhere!")
time.sleep(.5)

print("Approach the monster? Y/N")
answer = input()

if answer == 'Y' or answer == 'y':
    print("You look into your backpack...")
    checkPack()

    battleInit("Gelaton")

else:
    print("You ran away!")







