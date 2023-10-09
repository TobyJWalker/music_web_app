import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import *

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/albums', methods=['GET'])
def get_all_albums():
    conn = get_flask_database_connection(app)
    repo = AlbumRepository(conn)

    albums = repo.all()

    return '\n'.join([str(album) for album in albums])

@app.route('/albums/<id>', methods=['GET'])
def get_one_album(id):
    conn = get_flask_database_connection(app)
    repo = AlbumRepository(conn)

    return str(repo.find(id))

@app.route('/albums', methods=['POST'])
def create_new_album():
    conn = get_flask_database_connection(app)
    repo = AlbumRepository(conn)

    title = request.form['title']
    release_year = int(request.form['release_year'])
    artist_id = int(request.form['artist_id'])

    repo.create(title, release_year, artist_id)
    return '200'


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

