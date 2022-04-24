# about variables
my_age = 2022 - 1985
my_height = "5'10''"
print("I am ", my_age, " years old!")
print("I am ", my_height, "tall")


cars = 100
space_in_a_car = 4.0
drivers = 30
passangers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passanger_per_car = passangers / cars_driven

print("There are", cars, "cars avaiable!")
print("There are only", drivers, "drivers avaiable!")
print("One car has", space_in_a_car, "spaces!")
print("There are", passangers, "passangers today.")
print("We can transport ", carpool_capacity, "people today.")
print("We need to put about", average_passanger_per_car, "per car.")
