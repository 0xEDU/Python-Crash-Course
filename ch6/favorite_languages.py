# A dictionary of similar objects
favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}

# Looping through the entire dict
# for name, language in favorite_languages.items():
# 	print(f"{name.title()}'s favorite language is {language.title()}.")

# Looping through the dict's values
# keys() is not mandatory in this situation
# for name in favorite_languages.keys():
# 	print(name.title())

# Dict and list
# friends = ['phil','sarah']
# for name in favorite_languages.keys():
# 	print(name.title())
#
# 	if name in friends:
# 		language = favorite_languages[name].title()
# 		print(f"\t{name.title()}, I see you love {language}!")

# keys() returns a list of all the keys
# if 'erin' not in favorite_languages.keys():
# 	print("Erin, please take our poll!")

# Looping through a dict keys in a particular order, sorted()
# for name in sorted(favorite_languages.keys()):
# 	print(f"{name.title()}, thank you for taking the poll.")

# Looping through all values in a dict, if not specified, some may repeat
# print("The following languages have not been mentioned.")
# for language in favorite_languages.values():
# 	print(language.title())

# Looping through all values in dict, omitting repetitions.
print("The following languages have not been mentioned.")
for language in set(favorite_languages.values()):
	print(language.title())






