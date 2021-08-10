import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

#######################################################

artist1 = Artist("Bob Marley")
artist_repository.save(artist1)

artist2 = Artist("Rihanna")
artist_repository.save(artist2)

#######################################################

selected_artist = artist_repository.select(artist1.id)
print(selected_artist.__dict__)

#######################################################

artist_repository.select_all()
for artist in artist_repository.select_all():
    print(artist.__dict__)

#########################################################

# NOT WORKING
artist2.name = "Robyn"
artist_repository.update(artist2)

#########################################################

artist_repository.delete(artist1.id)


artist_repository.albums(artist2)

##########################################################

album1 = Album("Rihanna Album", "Pop", artist2)
album_repository.save(album1)

for album in album_repository.select_all():
    print(album.__dict__)

###########################################################

# album_repository.delete_all()
# artist_repository.delete_all()

############################################################

# album_repository.delete(album1.id)

#############################################################

album1.title = "albumzzzzz"
album_repository.update(album1)

pdb.set_trace()
