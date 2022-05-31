# 7.4 Exercise
prompt = ("\nEnter the pizza topping you would like to have.")
prompt += ("\nEnter 'quit' to end the program. ")

while True:
	message = input(prompt)
	if message == 'quit':
		break
	else:
		print(f"{message.title()} will be added to your pizza.")
