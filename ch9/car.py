# Working with Classes and Instances
class Car:
	""" A simple attemp to 	represent a car. """

	def __init__(self, make, model, year):
		""" Initialize attributes to describe a car. """
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		""" Return a neatly formatted descriptive name."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	# Modifying an Attribute's Value Through a Method
	def update_odometer(self, kilometrage):
		""" 
		Set the odometer reading to a given value.
		Reject the change if it attempts to roll odometer back.
		"""
		if kilometrage >= self.odometer_reading:
			self.odometer_reading = kilometrage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, kilometrage):
		""" Add the given amount to the odometer reading."""
		self.odometer_reading += kilometrage


	def read_odometer(self):
		""" Print a statement showing a car kilometrage"""
		print(f"This car has {self.odometer_reading} kilometers on it.")

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())

# Modifying an Attribute's Value Directly
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# Modifying an Attribute's Value Through a Method
# my_new_car.update_odometer()
# my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()