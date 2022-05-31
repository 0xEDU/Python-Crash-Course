# 6.9 Exercise		
favorite_places = {
	'edu':['são paulo', 'goiás'],
	'mari':['monte verde'],
	'melo':['tókio', 'rio de janeiro', 'são paulo'],
}

for person, places in favorite_places.items():
	print(f"\nO(s) lugar(es) favorito(s) de {person.title()} é: ")
	for place in places:
		print(f"{place.title()}")
