# number of cars
cars = 100
# amount of space in a car
space_in_a_car = 4
# number of drivers
drivers = 30
# number of passengers
passengers = 90
# number of cars not being driven
cars_not_driven = cars - drivers
# number of cars being driven
cars_driven = drivers
# how many people can fit in all of the cars driven
carpool_capacity = cars_driven * space_in_a_car
# average number of passengers in the driven cars
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put", average_passengers_per_car, "in each car.")
