# 5.10 Exercise
current_users = ['edu','MARI','pedro','gabriel','lucas']
new_users = ['mari','GABRIEL','mateus','diogo','luisa']
current_users_standardized = current_users[:]
current_users_standardized = [x.lower() for x in current_users_standardized]

for new_user in new_users:
	if new_user.lower() in current_users_standardized:
		print(f"{new_user.title()}, your username is already in use. Choose a new one.")
	else:
		print(f"Your username, {new_user.title()}, is available")