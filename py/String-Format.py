types_of_people = 10

# Using integer variable "types_of_people" in a fstring
x = f"There are {types_of_people} types of people."
binary = "binary"
do_not = "don't"

# Using strings in fstring
y = f"Those who know {binary} and those who {do_not}."

# Printing string validables
print(x)
print(y)

# Printing string validables
print(f"I said: {x}")
print(f"I also said :'{y}'")

# using string.format () - one of many ways

hilarious = "Really?"
joke_evaluation = "Isn't that joke funny?!{}"
print(joke_evaluation.format(hilarious))

# using string.format () - another way of achieving the same output in one line
print("Isn't that joke funny?!{}".format("Really?"))
print("Isn't that joke funny?!{}".format(hilarious))
