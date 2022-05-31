import random

nums = [12, 65, 15, 169, 123, 86, 57, 69, 95, 6, 'a', 'b', 'd', 'v', 'f']

x = 0
while True:
	r = random.choices(nums, k=4)
	x += 1
	if r == [12, 169, 123, 'a']:
		print(r)
		print(f"The loop ran {x} times.")
		break