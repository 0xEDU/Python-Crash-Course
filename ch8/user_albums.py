# 8.8 Exercise
def make_album(artist, title, num_songs=None):
	album = {'artist':artist, 'title':title}
	if num_songs:
		album['number of songs'] = num_songs
	return album

while True:
	print("\nEnter an album name, its artist's name and number of songs(optional)")
	print("Enter 'q' to quit")

	art_name = input("\nArtist name: ")
	if art_name == 'q':s
		break
	alb_title = input("Album title: ")
	if alb_title == 'q':
		break
	n_songs = input("Number  of songs: ")
	if n_songs == 'q':
		break

	if n_songs:
		build_album = make_album(art_name, alb_title, n_songs)
		print(build_album)
	else:
		build_album = make_album(art_name, alb_title)
		print(build_album)