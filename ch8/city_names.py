# 8.6 Exercise
def city_country(c_name, c_country):
	city = f"{c_name}, {c_country}."
	return city.title()

city1 = city_country('santiago', 'chile')
print(city1)

city2 = city_country('medellin', 'colombia')
print(city2)

city3 = city_country('são paulo', 'brasil')
print(city3)