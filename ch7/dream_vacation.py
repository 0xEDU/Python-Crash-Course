# 7.10 Exercise
responses = {}

active = True
while active:
	name = input("\nWhat is your name? ")
	response = input("Where would you go in a vacation? ")

	responses[name] = response
	
	repeat = input("\nWould you like to end(yes/no)? ")
	if repeat == 'yes':
		active = False

print("\n --- Result s---")
for name, response in responses.items():
	print(f"{name.title()} would like to go to {response.title()}.")