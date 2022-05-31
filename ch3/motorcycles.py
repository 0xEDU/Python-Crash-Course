# List with values + Append()
# motorcycles = ['honda','suzuki','yamaha']
# print(motorcycles)
#
# motorcycles.append('ducati')
# print(motorcycles)

# Empty list + Append()
# motorcycles = []
#
# motorcycles.append('ducati')
# motorcycles.append('honda')
# motorcycles.append('yamaha')
#
# print(motorcycles)

# Insert()
# motorcycles = ['honda','yamaha','suzuki']
# motorcycles.insert(0, 'ducati')
#
# print(motorcycles)

# Del
# motorcycles = ['honda','yamaha','suzuki']
# print(motorcycles)
#
# del motorcycles[1]
# print(motorcycles)

# Pop()
# motorcycles = ['honda','yamaha','suzuki']
# print(motorcycles)
#
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

# Pop() example
# motorcycles = ['honda','yamaha','suzuki']
#
# last_owned = motorcycles.pop(1)
# print(f"The last motorcycle I owned was a {last_owned.title()}.")

# Remove()
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")


