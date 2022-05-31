# Exercise 9.4
class Restaurant:
	""" A simple restaurant model. """

	def __init__(self, restaurant_name, cuisine_type):
		""" Initialize restaurant attributes"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(f"\nThe restaurant name is {self.restaurant_name}.")
		print(f"Its cuisine type is {self.cuisine_type}.")

	def set_number_served(self, served_clients):
		self.number_served = served_clients

	def print_number_served(self):
		print(f"The restaurant has served {self.number_served} clients.")

	def increment_number_served(self, served_clients):
		self.number_served += served_clients

	def open_restaurant(self):
		print("The restaurant is open!")

restaurant = Restaurant('mangai', 'brazilian')
restaurant.describe_restaurant()

restaurant.print_number_served()

restaurant.set_number_served(500)
restaurant.print_number_served()

restaurant.increment_number_served(100)
restaurant.print_number_served()