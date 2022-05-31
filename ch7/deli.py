# 7.8 Exercise
sandwich_orders = ['x-bacon', 'x-tudo', 'x-coração']
finished_sandwiches = []

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()

	print(f"I made your {current_sandwich}.")
	finished_sandwiches.append(current_sandwich)

print("Sandwiches made:")
for sandwich in finished_sandwiches:
	print(sandwich)