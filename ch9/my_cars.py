# from car_module import Car, ElectricCar

# my_beetle = Car('volkswagen', 'beetle', 2019)
# print(my_beetle.get_descriptive_name())

# my_tesla = ElectricCar('tesla', 'roadster', 2019)
# print(my_tesla.get_descriptive_name())

import car_module

my_beetle = car_module.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car_module.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())