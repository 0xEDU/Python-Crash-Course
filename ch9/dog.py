# Classes
#
# Class: A set of instructions for how to make an Instance.
# Instance: Object derived from a class(proccess called instatiation)
class Dog:
	""" A simple attempt to model a dog."""

	# Method: A function that is part of a class 
	def __init__(self, name, age):
	# __init__() is a special method, ran automatically by Python
		""" Initialize name and age attributes."""
		# Attributes: Variables accessible through an instance.
		self.name = name
		self.age = age

	def sit(self):
		""" Simulate a dog sitting in response to a command."""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		""" Simulate rolling over in response to a command."""
		print(f"{self.name} rolled over!")

# Making an Instance.
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)
# Dot is used access Attributes from an Instance
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

# Calling methods
# my_dog.sit()
# my_dog.roll_over()