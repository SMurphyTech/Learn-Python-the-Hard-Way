# defines the function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man, thats enough for a party!?")
    print("Get a blanket\n")

# gives regular numbers as arguments
print("We can just give the function numbers directly:")
cheese_and_crackers(2, 3000)

print("OR, we can use variables from our script:")
# defines variables
amount_of_cheese = 10
amount_of_crackers = 50

# gives variables as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
# uses solution to the math problems as arguments
cheese_and_crackers(10 - 4, 12 * 7)

print("And we can combine the two, variables and math:")
# combines math and variables
cheese_and_crackers(amount_of_cheese + 111, amount_of_crackers - 54)