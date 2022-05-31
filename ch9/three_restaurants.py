# 9.2 Exercise
class Restaurant:
	""" A simple restaurant model. """

	def __init__(self, restaurant_name, cuisine_type):
		""" Initialize restaurant name and cuisine type"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"\nThe restaurant name is {self.restaurant_name}.")
		print(f"Its cuisine type is {self.cuisine_type}.")

	def open_restaurant(self):
		print("The restaurant is open!")

res1 = Restaurant('do', 'japanese')
res2 = Restaurant('napa', 'italian')
res3 = Restaurant('mc donalds', 'american')

res1.describe_restaurant()
res2.describe_restaurant()
res3.describe_restaurant()