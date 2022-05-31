# 7.9 Exercise
sandwich_orders = ['pastrami', 'pastrami', 'pastrami', 'x-bacon', 'x-tudo', 'x-coração']
finished_sandwiches = []

print("We ran out of pastrami.")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()

	print(f"I made your {current_sandwich}.")
	finished_sandwiches.append(current_sandwich)

print("Sandwiches made:")
for sandwich in finished_sandwiches:
	print(sandwich)