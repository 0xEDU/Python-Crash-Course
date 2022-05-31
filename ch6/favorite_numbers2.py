# 6.11 Exercise
fav_nums = {
	'mari': [3, 9],
	'edu': [13, 22],
	'mat': [29, 34],
	'pedro': [14, 15],
	'luisa': [21, 29],
}

for name, nums in fav_nums.items():
	print("\n" + name.title())
	for num in nums:
		print(num)