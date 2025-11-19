# Tuesday Review #

# Define a new function fungus_among_us() which accepts a list `plants` as an argument
#   return True if the function contains the string "fungus" and False if not
# 	don't overthink this one, there's a very simple method to doing it...
#   Example: fungus_among_us( ["tree", "flower", "fungus", "moss"] ) >>> True

plants = ["tree", "flower", "fungus", "moss"]

def fungus_amongus(plants):
	for plant in plants:
		if plant == "fungus":
			return True
	return False

# Define a new function total_bill() which accepts a list of numbers `item_costs`
#   return the sum total of all items in the list
#   Example: total_bill( [6, 9.99, 20] ) >>> 35.99

# def total_bill(item_costs):
# 	return sum( item_costs )

total_bill = lambda item_costs: sum( item_costs )

# Define a new function halfway_there() which accepts a list of arbitrary data `items` longer than 1 item
#   insert the string "HALFWAY" at the middle of the list and return the altered list
# 	when inserting, you will need to make sure your index is an integer...
#   Example: halfway_there( [1,2,3,4,5,6] ) >>> [1,2,3,"HALFWAY",4,5,6]

def halfway_there(items):
	# floor operator //
	halfway = len(items) // 2
	# items[halfway] = 'HALFWAY'
	items.insert(halfway, 'HALFWAY')
	return items


# IMPORTING MODULES #

from robot import robot_uprising, Robot, Roomba

wall_e = Robot("WALL-E", "2000 years", "not that smart, he likes garbage")

# Afternoon Practice #

# RETURN AT 2:35 EST #

# in a new file create a class `Human` and import it into your current working file

# a `Human` needs these required attributes defined by its `__init__` method: `first_name:str`, `last_name:str`, `age:int`, `address:str`, `is_hungry:bool`

# a `Human` has a `__repr__` method that outputs their information like this: `Human( first_name=Bob last_name=Marley age=30 address=Jamaica is_hungry=False )`
	# don't forget `self`!

# a `Human` has a method named `full_name()` which returns a string that's a combination of their `first_name` and `last_name`

# a `Human` has a method named `order_drinks()` which returns `"Party time!"` if their age is 21 or higher and `"Denied"` if their age is less than that

# a `Human` has a method named `eat()` which sets their `is_hungry` attribute to `False`

# a `Human` has a method named `win_lottery()` which sets their `address` attribute to `"Disneyworld"`

# BONUS: utilize `**kargs` in order to take in and assign any attribute while creating a new `Human`

from human import Human