people = 2
cars = 17
trucks = 30


if cars > people:
    print("We should take the cars.")
# if the above if statements comes out to false, this elif is tested.
elif cars < people:
    print("We should not take the cars.")
# if the above elif statement comes out to false, the else runs
else:
    print("We can't decide.")
    
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")
    
if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home them.")