# 8.12 Exercise
def make_sandwich(*args):
	""" Summarize the items in a sandwich."""
	print("\nYour sandwich have the following:")
	for arg in args:
		print(f"- {arg}")

make_sandwich('cheese','tomato')
make_sandwich('cabbage', 'cheddar', 'pepperoni')
make_sandwich('cheddar','cheese','muzzarella','camembert')