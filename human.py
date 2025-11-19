class Human:

	def __init__(self, first_name, last_name, age, address, is_hungry, **kargs):
		print("I AM ALIVE")
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.address = address
		self.is_hungry = is_hungry
		for key, val in kargs.items():
			setattr( self, key, val )

	def __repr__(self):
		return f"Human( first_name={self.first_name} last_name={self.last_name} age={self.age} address={self.address} is_hungry={self.is_hungry} )"
	
	def full_name(self):
		return f"{self.first_name} {self.last_name}"
	
	def order_drinks(self):
		if self.age >= 21:
			return "Party time!"
		else:
			return "Denied"
		
	def eat(self):
		self.is_hungry = False

	def win_lottery(self):
		self.address = "Disneyworld"

	def change_first_name(self):
		self.first_name = input('Change Name >>> ')