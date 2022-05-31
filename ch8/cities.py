# 8.5 Exercise
def describe_city(city_name, country='Brazil'):
	""" Print a simple sentence """
	print(f"{city_name.title()} is in {country.title()}.")

describe_city('são paulo')
describe_city('goiânia')
describe_city('montevideo', 'uruguay')