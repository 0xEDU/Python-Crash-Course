# 8.10 Exercise
def show_messages(messages):
	""" Print every element in a list."""
	print("Messages in the list:")
	for msg in messages:
		print(f"\t{msg}")

def send_messages(messages, sent_messages):
	print("\n")
	while messages:
		sending_message = messages.pop()
		print(f"Sending message {sending_message}")
		sent_messages.append(sending_message) 

messages = ['oi', 'tchau', 'até', 'bom dia']
sent_messages = []

show_messages(messages)
send_messages(messages, sent_messages)

print(messages)
print(sent_messages)