# 5.1 and 5.2 Exercises modified
cars = ['subaru','audi','bmw','volkswagen']

print("Is there a subaru in the list? I predict True.")
if 'subaru' in cars:
	print('subaru' in cars)

print("\nThe list is: ")
for car in cars:
	if 'subaru' in car:
		print("*There is a subaru in the list.*")
	if 'bmw' in car:
			print(car.upper())
	else:
		print(f"{car.title()}")


if cars != 'banana':
	print("\nCars are not bananas!")