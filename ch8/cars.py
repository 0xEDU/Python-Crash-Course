# 8.14 Exercise
def make_car(manufacturer, model_name, **kwargs):
	kwargs['manufacturer'] = manufacturer
	kwargs['model_name'] = model_name
	return kwargs

car_profile = make_car('toyota', 'prius', year=2018, color='black',)
print(car_profile)