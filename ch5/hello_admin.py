# 5.8 and 5.9 Exercises
users = ['edu','mari','admin','pedro','gabriel']

if users:
	for user in users:
		if 'admin' in user:
			print(f"Hello, {user.title()}, would you like to see a status report?")
		else:
			print(f"Hello, {user.title()}!")
else:
	print("We need to find some users!")