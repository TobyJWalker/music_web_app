from lib.album_repository import *
from lib.artist_repository import *

# Tests for your routes go here

def test_list_all_albums(web_client, db_connection):
    db_connection.seed('seeds/music_library.sql')
    response = web_client.get('/albums')

    assert response.status_code == 200
    assert 'Album(1, Doolittle, 1989, 1)' in response.data.decode('utf-8')

def test_create_album(web_client, db_connection):
    db_connection.seed('seeds/music_library.sql')

    response = web_client.post('/albums', data={
        'title': 'Voyage',
        'release_year': 2022,
        'artist_id': 2
    })

    assert response.status_code == 200
    assert 'Voyage' in web_client.get('/albums').data.decode()

def test_get_one_album(web_client, db_connection):
    db_connection.seed('seeds/music_library.sql')

    response = web_client.get('/albums/1')

    assert response.status_code == 200
    assert response.data.decode() == 'Album(1, Doolittle, 1989, 1)'

def test_list_all_artists(web_client, db_connection):
    db_connection.seed('seeds/music_library.sql')
    response = web_client.get('/artists')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone'

def test_create_artist(web_client, db_connection):
    db_connection.seed('seeds/music_library.sql')
    response = web_client.post('/artists', data={
        'name': 'The Beatles',
        'genre': 'Rock'
    })

    assert response.status_code == 200
    assert 'The Beatles' in web_client.get('/artists').data.decode('utf-8')