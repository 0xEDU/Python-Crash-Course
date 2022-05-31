"""A set of classes used to represent cars, batteries and electric cars."""

class Car:
	""" A simple attemp to 	represent a car. """

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def update_odometer(self, kilometrage):
		if kilometrage >= self.odometer_reading:
			self.odometer_reading = kilometrage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, kilometrage):
		self.odometer_reading += kilometrage

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} kilometers on it.")

	def fill_gas_tank(self):
		print("This car needs to refuel")

class Battery:
	def __init__(self, battery_size=75):
		""" A simple attempt to model a battery for a electric car."""
		self.battery_size = battery_size

	def describe_battery(self):
		""" Print a statement describing the battery."""
		print(f"This car has a {self.battery_size}-kWh battery.")

	def get_range(self):
		""" Print a statement about the range this battery provides."""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315

		print(f"This car can go about {range} kilometers on a full charge.")

	def upgrade_battery(self):
		if self.battery_size < 100:
			self.battery_size = 100

class ElectricCar(Car):
	""" Reperesent the aspects of a car, specific to electric vehicles """

	def __init__(self, make, model, year):
		""" 
		Initialize the attributes of the parent class.
		Then initialize attributes specific to an electric car.
		"""
		super().__init__(make, model, year)
		self.battery = Battery()

	def fill_gas_tank(self):
		""" Electric cars don't have gas tanks."""
		print("This car doesn't need gas tanks.")