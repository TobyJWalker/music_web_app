from lib.album import Album

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []

        for row in rows:
            albums.append(Album(row["id"], row["title"], row["release_year"], row["artist_id"]))
        
        return albums

    def find(self, id):
        rows = self._connection.execute(f'SELECT * FROM albums WHERE id={id}')
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])
    
    def create(self, title, release_year, artist_id):
        self._connection.execute(f"INSERT INTO albums (title, release_year, artist_id) VALUES ('{title}', {release_year}, {artist_id})")

    def delete(self, id):
        self._connection.execute(f"DELETE FROM albums WHERE id = {id}")