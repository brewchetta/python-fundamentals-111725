# Wednesday Review #

# RETURN AT 11:00 EST

# Create a class `MovieReview` which has required attributes `movie_title:str`, `reviewer_name:str`, `score:int`, `date_reviewed:datetime.date`.
	# You may need to look up how to use `datetime.date` (hint: you'll need `from datetime import date`)

# Create an instance method `pretty_print()` which prints the review like so: `"<movie_title> review by <reviewer_name> on <date_reviewed>: <score> / 5 stars"`.
	# Example: `land_before_time.pretty_print()` >>> `"Land Before Time review by Fred Flintstone on 2014-4-12: 5/5 stars"`

# Create an instance method `increase_score()` which increases that movie's score by 1 but not above 5.

# Create an instance method `update_review()`. This accepts an argument of a `new_score` and optionally a `new_reviewer`. This updates the `score` and sets the `date_reviewed` to today.  If `new_reviewer` was passed this will also update the `reviewer_name` and if not it will retain the previous `reviewer_name`.
	# Example: `land_before_time.update_review(4)` # score changed to `4`, date becomes today, reviewer is still `"Fred Flinstone"`
	# Example: `land_before_time.update_review(5, "Littlefoot")` # score changed to `5`, date becomes today, reviewer becomes `"Littlefoot"`

# Create a class method `review_bomb()` which accepts a `movie_title` and `num_reviews`. This generates a review `num_reviews` times for the `movie_title` each with a `score` of 1, a `reviewer_name` of `Statler & Waldorf`, and a `date_reviewed` of today. Return all instances in a list.
	# Example: `MovieReview.review_bomb("Plan 9 From Outer Space", 10)` >>> creates 10 reviews for "Plan 9 From Outer Space"

from datetime import date
from movie_reviews import MovieReview

predator = MovieReview(movie_title="Predator", reviewer_name="Chett", date_reviewed=date.today(), score=4)






# ERROR HANDLING #

def divide_numbers(num_one, num_two):
	try: # do this if you can
		if type(num_one) != int or type(num_two) != int:
			# this will artificially trigger an error
			raise TypeError("Why would you give me anything that's not an integer HOW DARE YOU")
		print(num_one / num_two)
	except ZeroDivisionError: # do this if you got a ZeroDivisionError
		print(f"could not divide {num_one} by {num_two}")
	except TypeError as the_error_we_got: # do this if you got a TypeError (like the one we raise above)
		print(f"We got a type error!")
		print(the_error_we_got)
	finally: # this will happen after either of the above triggers
		print("FUNCTION DONE")

def cube_number(number):
	try:
		return number ** 3
	except TypeError:
		return "This data type cannot be cubed"

# try:
# 	divided_by_zero = 100 / 0
# except:
# 	print("I could not divide by zero... WOMP WOMP")

# print("I am below the error")


# HTTP REQUESTS #

import requests

def get_dad_joke():
	try:
		response = requests.get("http://icanhazdadjoke.com", headers={ "Accept": "text/plain" })
		joke_text = response.text
		return joke_text
	except:
		print("Unable to fetch dad joke")

# new_joke = get_dad_joke()

def fetch_number_of_jokes(num_jokes):
	jokes_list = []
	for _ in range(num_jokes):
		fetched_joked = get_dad_joke()
		jokes_list.append( fetched_joked )
	return jokes_list


# WRITING TO JSON FILES #

import json

def put_into_json_file(list_data):
	current_jokes = get_from_json_file()
	with open('jokes.json', 'w') as json_file:
		combined_jokes = current_jokes + list_data
		json.dump( combined_jokes, json_file, indent=4 )


def get_from_json_file():
	with open('jokes.json', 'r') as json_file:
		data = json.load(json_file)
		return data


# BUILDING PROGRAM #

# user stories --> a user will be able to...

# a user will be able to boot up the program and see a menu
# a user will be able to fetch a new dad joke
# a user will be able to save or discard a fetched dad joke
# a user will be able to see their saved dad jokes
# a user will be able to exit the program

import time

class DadJokeApplication:

	running = True

	def run(self):
		while self.running:
			self.menu()
			user_choice = input("Please choose an option: ")
			print( "You chose: ", user_choice )
			if user_choice == "1":
				self.get_dad_joke()
			elif user_choice == "2":
				self.print_saved_dad_jokes()
			elif user_choice == "3":
				self.exit()
			else:
				time.sleep(1)
				print("\nPlease choose a valid option! (╯°□°)╯︵ ┻━┻\n")

	def menu(self):
		print("--Welcome to the Dad Jokes App--")
		print("1. Get new dad joke")
		print("2. See saved dad jokes")
		print("3. Exit")

	def get_dad_joke(self):
		time.sleep(1)
		new_joke = fetch_number_of_jokes(1)
		print(new_joke)
		user_input = input("Save joke? [y/n]")
		if user_input == 'y':
			time.sleep(1)
			print("Saving this gem of a joke!")
			put_into_json_file(new_joke)
		else:
			time.sleep(1)
			print("Discarding the joke...")

	def print_saved_dad_jokes(self):
		time.sleep(1)
		print("------------------------------------")
		saved_jokes = get_from_json_file()
		for joke in saved_jokes:
			print(joke)
		print("------------------------------------")
		time.sleep(1)

	def exit(self):
		time.sleep(1)
		self.running = False
		print("\nSee ya later alligator\nIn a while crocodile")

app = DadJokeApplication()
app.run()