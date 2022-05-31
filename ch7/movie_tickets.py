# 7.4 Exercise
msg = ("\nWhat is your age?")
msg += ("\nEnter '777' to exit. ")


while True:
	age = int(input(msg))
	if age < 3:
		ticket = 0
	elif age <= 12:
		ticket = 10
	elif age > 12:
		ticket = 15
	elif age == 777:

	print(f"Your ticket costs ${ticket}.")