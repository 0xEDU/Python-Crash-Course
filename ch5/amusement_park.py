#IF-ELIF-ELSE
age = 70

if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
elif age >= 65:
	price = 20
# ELSE is not necessary to end the elif chain
# else:
# 	price = 20

print(f"Your admission cost is ${price}.")