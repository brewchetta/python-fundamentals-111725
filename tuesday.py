# Monday Review Practice #

# Define a new function create_full_name() which takes in two arguments: first_name and last_name as strings
# 	the function returns the first_name and last_name as a single string
# 	Example:	create_full_name("Bob", "Marley") >>> "Bob Marley"

def create_full_name(first_name:str, last_name:str):
	return first_name + " " + last_name

full_name = create_full_name("Chett", "Tiller")

# print(full_name)

# Define a new function c_to_f() which takes in one argument: temp_celsius as a number
# 	the function returns the temperature as farenheit, you may return either an int or a float
# 	the formula for conversion is F = (C * 9/5) + 32
# 	Example:	c_to_f(30) >>> 86.0

def c_to_f(temp_celsius:int):
	return (temp_celsius * 9 / 5) + 32

# farenheit = c_to_f(100)
# print(farenheit)

# farenheit = c_to_f(0)
# print(farenheit)

# farenheit = c_to_f(30)
# print(farenheit)

# farenheit = c_to_f(26.4)
# print(farenheit)

# Define a new function open_thieves_cave() which takes in one argument: passphrase as a string
# 	the function returns True if the passphrase is "open sesame" and False if the passphrase is anything else
# 	Example:	open_thieves_cave("open sesame") >>> True
# 	Example:	open_thieves_cave("speak friend and enter") >>> False

def open_thieves_cave(passphrase:str):
	if passphrase == "open sesame":
		return True
	else:
		return False

# result = open_thieves_cave("open sesame")
# print(result)

# result = open_thieves_cave("password")
# print(result)

# result = open_thieves_cave(12)
# print(result)

# For these functions do not worry about edge cases; assume the functions will receive the proper data type
# For example you don't need to worry about giving c_to_f a string


# LIST #

# lists are a collection of data
sodas = [ "Coke", "Pepsi", "Dr Pepper", "Sprite" ]

# index - where it is in the list
# we can access an item by its index
# indexes start at 0 and they must be integers
# if we have negative indexes (except 0) they will count from the end instead of the beginning

sodas[0] # "Coke"
sodas[3] or sodas[-1] # "Sprite"

sodas[1] = "Root Beer"

# you may use different types of data in a list
different_stuff = [True, "whatever", 12, 12.0, [], "THE END"]

# a list with sub-lists
listception = [[1,2,3],[4,5,6],[7,8,9]]

# you can also put in line breaks if you feel like it
listception = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]

# this will access the first list's second element
listception[0][1] # 2

# this will show how many sodas are in the list
len(sodas) # 4

# how do we add to the end of a list?
sodas.append("Fanta")
sodas.append("Cream Soda")

# this will show how many sodas are in the list
len(sodas) # 6

# this will add a new element at index zero and shift the other items behind it by one index
sodas.insert(0, "Diet Coke Zero")

# if I want to sort....
sodas.sort() # will sort alphabetically

# to remove the last item...
sodas.pop()

# to remove an item by its index
sodas.pop(3)

# def plus_one(x):
# 	return x + 1

# lambdas - short one line function - a lambda automatically "implicitly" returns
plus_one = lambda x: x + 1

create_fullname = lambda first_name,last_name: first_name + " " + last_name

# higher order function - takes in a function and does something with it
def do_three_times(fn):
	fn()
	fn()
	fn()

def say_hi():
	print("HI")

pass_in_3 = lambda fn: fn(3)


filtered_result = filter(lambda soda: soda == "Diet Coke Zero", sodas)
filtered_sodas = list(filtered_result)

# Exercises # Return at 12:40 EST

# Create a new list with three pieces of furniture >>> ["chair", "table", "bed"]

# Access the second furniture item in the list
# Access the last furniture item in the list

# Use python to check the length of the list
# Add three new furniture items to the list
# Use python to check the length of the list

# Add a new furniture item to the beginning of the list
# Add a new furniture item as the 3rd item in the list

# Sort the list

# Remove the second to last item in the list

# Remove a "chair" from the list if it exists

# Use python to check the length of the list

# Look up a way to count the number of times "bed" appears in the list
	# we only want "bed" exactly, don't worry about things like "waterbed"

# Look up a way to reverse the order of the list

# Look up a way to clear the entire list


# TUPLE #

# we may not alter or mutate the tuple
# when we create the tuple it will be like this until the program ends
my_tuple = ("pizza", "hamburger", "hotdog", "salad")


# SET #

# sets are unordered unique data
my_set = { 1,2,3,4,5,6,7,7,7,7,7,7 } # {1,2,3,4,5,6,7}

# DICTIONARIES #

my_dict = { 'key': 'value' }

person = { 
	'first_name': 'Chett', 
	'last_name': 'Tiller', 
	'height': '1000 feet tall', 
	'age': 21,
	'favorite_sodas': ['Coke', 'Pepsi'],
	'password': 'password123',
	'favorite_person': {
		'first_name': 'Bob',
		'age': 12
	}
}

person['height'] # accesses the height in the dict

# person['fav_movie'] # will result in a key error

person.get('fav_movie') # will not result in a key error

person['first_name'] = "Boba Chett"

person['favorite_movie'] = "The Land Before Time"

def legally_able_to_drive(person:dict):
	return person['age'] >= 16


# LOOPS and ITERATION #

# for loops will iterate through every item in an iterable starting at the beginning
# `item` is just a variable name, you may use almost any name instead
for item in sodas:
	# print( item )
	pass


# while loops will continue their block of code over and over until their condition is False 
index = 0
while index < len( sodas ):
	# print(sodas[index])
	index += 1


# list comprehension

# generates a new list based off an old one
# `sodas` and `my_numbers` are iterables
# `item` or `s` or `num` is just a variable name and you may use anything that isn't a reserved keyword
empty_sodas = [ ("Empty " + item) for item in sodas ]

shaken_sodas = [ (soda_to_shake + " EXPLOSION") for soda_to_shake in sodas ]

my_numbers = [1,2,3,4,5]
squared = [ num * num for num in my_numbers ]

# Afternoon Guided Exercise #

# new function called fizz_buzz_list
# this accepts a list of numbers as an argument
# with the list I want to see for each item inside whether that item is cleanly divisible by 3 or 5
# if the number is divisible by 3 we replace the item with "Fizz"
# if the number is divisible by 5 we replace the item with "Buzz"
# if the number is divisible by 3 AND 5 we replace the item with "Fizz Buzz"
# if not divisible by either we leave the number as is
# return the altered list

test_case_one = [1,2,3,6,7,8,15]

test_case_two = [52, 55, 98, 133]

test_case_three = [6081, 1200, 134, 547, 896, -200, -35, -6081, 0]

# def fizz_buzz_list(list_of_numbers):
# 	for number in list_of_numbers:
# 		index = list_of_numbers.index(number)
# 		if number % 3 == 0 and number % 5 == 0:
# 			list_of_numbers[index] = 'Fizz Buzz'
# 		# if the number is divisible by three
# 		elif number % 3 == 0:
# 			# replace the number with Fizz by first getting its index
# 			list_of_numbers[index] = 'Fizz'
# 		elif number % 5 == 0:
# 			list_of_numbers[index] = 'Buzz'

# 	return list_of_numbers

def fizz_buzz_list(list_of_numbers):
	index = 0
	while index < len( list_of_numbers ):
		divisible_by_three = list_of_numbers[index] % 3 == 0
		divisible_by_five = list_of_numbers[index] % 5 == 0
		if divisible_by_three and divisible_by_five:
			list_of_numbers[index] = 'Fizz Buzz'
		elif divisible_by_three:
			list_of_numbers[index] = 'Fizz'
		elif divisible_by_five:
			list_of_numbers[index] = 'Buzz'
		index += 1
	return list_of_numbers

# modulo operator - %