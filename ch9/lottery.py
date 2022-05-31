import random

nums = [12, 65, 15, 169, 123, 86, 57, 69, 95, 6, 'a', 'b', 'd', 'v', 'f']

r = random.choices(nums, k=4)
print(f"The ticket matching the numbers and letter: {r} will win a prize!")