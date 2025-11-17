# Part 1  -----------Variables & Data Types ------------ #

# comment - a lil note just for you
# a comment does not get read by python

# variable
# given it a name - uses snake case
# given it a value
# variable_name = "hello world"
# 				# string - a piece of text

# define variables
# my_favorite_dad_joke = "Why did the scarecrow win an award? Because he was outstanding in his field!"

# question = 'What do you call fake spaghetti?'
# answer = 'An "impasta"'

# formatted_jokes = f"{ question } { answer }"

# concatenated_joke = formatted_joke + ". " + my_favorite_dad_joke

# print( my_favorite_dad_joke )

# print(formatted_jokes)

# integer
# number_of_snakes = 12

# number_of_snakes = 8

# print( number_of_snakes )

# floating point number / float
# average_number_of_snakes = 9.8

# print( number_of_snakes )

# boolean
# true / false
# i_am_true = True
# i_am_false = False

# first_name = "Chett"
# last_name = 12

# first_name_is_not_string = type( first_name ) != str
# last_name_is_not_string = type( last_name ) != str

# conditionals
# if first_name == "Chett" and last_name == "Henry":
#     print( "Welcome Chett Henry" )

#     if number_of_snakes >= 10:
#         print("You have a lot of snakes today Chett")

# elif first_name_is_not_string or last_name_is_not_string:
# 	print( "ENTRIES MUST BE TEXT" )
# elif first_name:
# 	print( "Hello stranger" )
# else:
# 	print("EMPTY FIRST NAME TRY AGAIN")

# ######################################################################### #

# Part 2 --- FUNCTIONS ------ #

# define a function
def say_hello():
	# put whatever the function does right here
	print("hello")

# call function
# what_we_get = say_hello()

# print( what_we_get )

# def add_one_plus_one():
# 	return 1 + 1

# what_we_get = add_one_plus_one()

# print( what_we_get )

# # function with parameters
# def add( number_one:int, number_two:int ):
# 	return number_one + number_two

# # invoking with arguments
# result = add( 1, 6 )

# def multiply(a, b, c=""):
# 	return a * b * c

# result_two = multiply(5, 2)

# print( result_two )

# def dad_joke_creator( question:str, punchline:str ):
# 	return f"{question} {punchline} :D"

# dad_joke = dad_joke_creator("Why can't your nose be 12 inches long?", "Because then it would be a foot!")

# print( dad_joke )

# # scope


# # using the global variable
# def think_about_thoughts():
# 	global outside_thoughts
# 	outside_thoughts = outside_thoughts + " but I would like a sportscar"

# think_about_thoughts()
# think_about_thoughts()
# think_about_thoughts()
# think_about_thoughts()
# think_about_thoughts()

# print( outside_thoughts )

# outside_thoughts = "I am happy and well adjusted"

# def think_inside_thoughts():
	# we have declared a new variable called outside_thoughts in the local scope
	# outside_thoughts = "I am an outside thought I think"
	# print( outside_thoughts )

# pull the global variable without altering it
# def think_my_outside_thoughts():
# 	print( outside_thoughts )

# think_my_outside_thoughts()

# print(outside_thoughts)

# you can only return one time in a function
# def multiple_returns():
# 	# this first return ends the function execution
# 	return "I am the return"
# 	# these other returns have NO EFFECT
# 	return "I'll be back"
# 	return "MORE RETURNS"
# 	return "EVEN MORE RETURNS"

# result = multiple_returns()

# print( result )

def login(username:str, password:str):
	if username and password:
		correct_username = "user123"
		correct_password = "password123"
		if username == correct_username and password == correct_password:
			return True

	return False

logged_in = login("user123", "password123") # True
print( "Logged in: ", logged_in )

logged_in = login("henry123", "password123") # False
print( "Logged in: ", logged_in )

logged_in = login("", "") # False
print( "Logged in: ", logged_in )


def passable_function():
	pass






# PRACTICE #


# UNTIL 3:50pm EST

# takes in the total price of the meal, 
# you can optionally add a tip, 
# if there are multiple people divide the grand total by the number of people
# your output should be a float

# edge cases
# what happens if someone puts in something that ISNT a number
# what happens if the number of people is 0

def restaurant_bill_calculator(total:float, number_of_guests:int=1, tip_percentage:float=0.0):

	if type(total) == int and type(number_of_guests) == int and  type(tip_percentage) == float:
		if number_of_guests > 0:
			subtotal = total * (1 + tip_percentage)
			per_guest_total = subtotal / number_of_guests
			return float(per_guest_total)
		else:
			return "get some friends"
	else:
		return "incorrect data types try again"

the_bill = restaurant_bill_calculator(50, 1, 0.0)
print( "the bill:", the_bill )

the_bill = restaurant_bill_calculator(50, 2, 0.0)
print( "the bill:", the_bill )

the_bill = restaurant_bill_calculator(50, 2, 0.20)
print( "the bill:", the_bill )

the_bill = restaurant_bill_calculator(50)
print( "the bill:", the_bill )

the_bill = restaurant_bill_calculator(50, 0)
print( "the bill:", the_bill )

the_bill = restaurant_bill_calculator("50 buckos", 5)
print( "the bill:", the_bill )

the_bill = restaurant_bill_calculator(50, "maybe between six and fifteen we'll see")
print( "the bill:", the_bill )