# Using input()
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# Letting the user choose when to kit
# prompt = "\nTell me something, and I will repeat it back to you."
# prompt += "\nEnter 'quit' to exit the program. "
#
# message = ""
# while message != 'quit':
# 	message = input(prompt)
#
# 	if message != 'quit':
# 		print(message)

# Using a flag
prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to exit the program. "

active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(messageN)