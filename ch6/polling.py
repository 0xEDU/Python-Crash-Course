favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}

take_poll = ['karen','jen','edward','lucy']
for people in take_poll:
	if people in favorite_languages.keys():
		print(f"{people.title()}, thank you for taking the poll.")
	elif people not in favorite_languages.keys():
		print(f"{people.title()}, you need to take the poll.")