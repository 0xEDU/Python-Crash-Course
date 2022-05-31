pet_0 = {
	'name': 'agata',
	'animal': 'cat',
	'owner': 'mari',
}

pet_1 = {
	'name': 'mingau',
	'animal': 'cat',
	'owner': 'lucas',
}

pet_2 = {
	'name': 'quica',
	'animal': 'dog',
	'owner': 'cris',
}

pets = [pet_0, pet_1, pet_2]
for pet in pets:
	print(f"It is a {pet['animal']}, called {pet['name'].title()}, " 
		f"owned by {pet['owner'].title()}")