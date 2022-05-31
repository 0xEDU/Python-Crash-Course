# 6.7 Exercise
mari = {
	'first_name':'Marina',
	'last_name':'Kehl',
	'age': 19,
	'city':'São Paulo',
}

edu = {
	'first_name':'Eduardo',
	'last_name':'Tachotte',
	'age': 19,
	'city':'Brasília',
}

pedro = {
	'first_name':'Pedro',
	'last_name':'Machado',
	'age': 21,
	'city':'São Paulo',
}

people = [mari, edu, pedro]
print("As pessoas que conheço são: ")
for person in people:
	full_name = f"{person['first_name']} {person['last_name']}"
	age = f"{person['age']}"
	city = f"{person['city']}"
	print(full_name, age, city)