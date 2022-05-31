# 6.3 and 6.4 Exercises
words = {
	'input':'user does stuff',
	'output':'computer does stuff',
	'nested':'one inside the other',
	'loop':'repeating stuff over and over',
	'tuple':'static list',
}

for word, meaning in words.items():
	print(f"{word.title()}: {meaning.title()}.")
