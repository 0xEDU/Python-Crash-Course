# 9.1 and 9.6 Exercises
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

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type, flavors):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = flavors

	def display_flavors(self):
		print("The flavors are:")
		print("")
		for self.flavor in self.flavors:
			print(f"{self.flavor.title()}")


# restaurant = Restaurant('habibs', 'arab')
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)

# restaurant.describe_restaurant()
# restaurant.open_restaurant()

list_flavors = ['pineapple', 'chocolate', 'strawberry']
icecream_shop = IceCreamStand('batates','ice cream', list_flavors)

icecream_shop.display_flavors()