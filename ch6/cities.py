cities = {
	'santo andré': {
		'country':'brasil',
		'pop':720000,
		'fact':'industrial city',
	},
	'são paulo': {
		'country':'brasil',
		'pop':10000000,
		'fact':"brazil's largest city",
	},
	'brasília': {
		'country':'brasil',
		'pop':1000000,
		'fact':"brazil's capital",
	},
}

for city, city_info in cities.items():
	country = city_info['country']
	pop = city_info['pop']
	fact = city_info['fact']
	
	print("\n" + f"{city.title()}:")
	print(country.title(), pop, fact)
	