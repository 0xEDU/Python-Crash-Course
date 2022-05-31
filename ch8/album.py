# 8.7 Exercise
def make_album(artist, title, num_songs=None):
	album = {'artist':artist, 'title':title}
	if num_songs:
		album['number of songs'] = num_songs
	return album

album1 = make_album('baco exu do blues', 'qvvjfa?', num_songs=12)
print(album1)

album2 = make_album('baco exu do blues', 'esú')
print(album2)

album3 = make_album('baco exu do blues', 'blvesman')
print(album3)