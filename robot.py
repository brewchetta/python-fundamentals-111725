def robot_uprising():
	print( "BEEP BOOP EXTERMINATE" )

# a class is a blueprint that makes instances of that new data type / class
class Robot:
	#  all robots start with this attribute unless we change them
	consistency = "metal"

	# init stands for initialize and runs whenever we initialize a new instance of the class
	def __init__(self, name, battery_life, processing_power, *args, **kargs):
		print("BEEP BOOP MAKING A NEW ROBOT")
		# print(**kargs)
		# this is generally used for assigning attributes when we make a new instance
		self.name = name
		self.battery_life = battery_life
		self.processing_power = processing_power
		for key in kargs:
			setattr(self, key, kargs[key])

	# representation that will show when we print the robot
	def __repr__(self):
		return f"Robot( name={self.name} battery_life={self.battery_life} processing_power={self.processing_power} )"
	
	# what we see when we print() or make our instance into a string with str()
	def __str__(self):
		return f"HELLO I AM A ROBOT NAMED {self.name}"

	# a method (a function attached to a class) must pass in 'self' which references itself
	def beep(self):
		return "BEEP"
	
	def bend(self):
		return "BENDING"
	
	def move(self):
		return f"I AM MOVING : I AM {self}"
	
	def analyze_info(self, info):
		return f"BEEP BOOP ANALYZING {info}"

	# the @ sign is a decorator
	# a decorator modifies the function after it
	@classmethod	
	def build_killer_robot(cls, name):
		print(cls)
		new_bot = Robot(name=name, battery_life="way too long", processing_power="kill", mode="destroy all humans")
		new_bot.consistency="aluminum"
		return new_bot
	

# D.R.Y - Dont Repeat Yourself

# the Roomba inherits from Robot (you could say its a type of robot)
class Roomba( Robot ):

	consistency = "cheap plastic"

	# will overwrite the repr just for the Roomba
	def __repr__(self):
		return f"Roomba( name={self.name} battery_life={self.battery_life} processing_power={self.processing_power} )"
	
	def vacuum(self):
		return "VRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR BUMP BUMP BUMP"