# 7.6 Exercise
msg = ("\nWhat is your age?")
msg += ("\nEnter 'quit' to exit. ")


# User stop
# while True:
# 	age = input(msg)
#
# 	if age == 'quit':
# 		break
# 	elif int(age) < 3:
# 		ticket = 0
# 	elif int(age) <= 12:
# 		ticket = 10
# 	elif int(age) > 12:
# 		ticket = 15
# 	print(f"Your ticket costs ${ticket}.")

# Flag stop
# active = True
# while active:
# 	age = input(msg)
#
# 	if int(age) < 3:
# 		ticket = 0
# 	elif int(age) <= 12:
# 		ticket = 10
# 	elif int(age) > 12:
# 		ticket = 15
#	
# 	print(f"Your ticket costs ${ticket}.")
# 	active = False

# Conditional stop
while True:
	age = input(msg)

	if age == 'quit':
		break
	elif int(age) < 3:
		ticket = 0
	elif int(age) <= 12:
		ticket = 10
	elif int(age) > 12:
		ticket = 15
	print(f"Your ticket costs ${ticket}.")












