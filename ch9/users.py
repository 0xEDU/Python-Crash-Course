# 9.3, 9.5, 9.7 and 9.8 Exercises
class User:
	""" A simple user profile."""
	def __init__(self, first_name, last_name, age, location):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location =	location
		self.login_attempts = 0
	
	def describe_user(self):
		print("\nUser info:")
		print(f"{self.first_name} {self.last_name}")
		print(f"{self.age} years old.")
		print(f"Lives in {self.location}.")

	def increment_login_attempts(self, attempt):
		self.login_attempts += attempt

	def reset_logins_attempts(self):
		self.login_attempts = 0

	def greet_user(self):
		print(f"Hello, {self.first_name}!")

class Privileges:
	def __init__(self, privileges):
		self.privileges = privileges
		
	def show_privileges(self):
		print("Privileges:")
		for self.privilege in self.privileges:
			print(f"- {self.privilege}")

class Admin(User):
	def __init__(self, first_name, last_name, age, location):
		super().__init__(first_name, last_name, age, location)
		self.privileges = Privileges(list_of_privileges)


#u1 = User('vinicius', 'silva', '19', 'brazil')
#u2 = User('gabriel', 'pereira', '18', 'germany')
#u3 = User('luisa', 'borges', '21', 'portugal')
#
# u1.describe_user()
# u1.greet_user()
#
# u2.describe_user()
# u2.greet_user()
#
# u3.describe_user()
# u3.greet_user()

## print(u1.login_attempts)
##
## u1.increment_login_attempts(1)
## u1.increment_login_attempts(1)
## u1.increment_login_attempts(1)
##
## print(u1.login_attempts)
## u1.reset_logins_attempts()
## print(u1.login_attempts)

### list_of_privileges = ['read', 'write', 'execute']
### admin = Admin('edu', 'tctt', '19', 'brazil', list_of_privileges)
### admin.show_privileges()

list_of_privileges = ['read', 'write', 'execute']
admin = Admin('edu', 'tctt', '19', 'brazil')
admin.privileges.show_privileges()
