# 9.13 Exercise
from random import randint

class Die:
	"""A simple model of a die, with a 'roll' system."""
	def __init__(self, sides):
		self.sides = sides

	def roll_die(self):
		num = randint(1, self.sides)
		print(num)

print("Die 1:")
die1 = Die(6)
x = 0
while x <= 9:
	die1.roll_die()
	x += 1

print("\nDie 2:")
die2 = Die(10)
x = 0
while x <= 9:
	die2.roll_die()
	x += 1

print("\n Die 3:")
die3 = Die(20)
x = 0
while x <= 9:
	die3.roll_die()
	x += 1