# Reading an entire file
# with open('pi_digits.txt') as file_object:
# 	contents = file_object.read()
# print(contents)

# Reading line by line
filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())