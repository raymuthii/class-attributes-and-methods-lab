class Song:
    count = 0  # Class attribute to keep track of the number of songs
    genres = []  # Class attribute for unique genres
    artists = []  # Class attribute for unique artists
    genre_count = {}  # Class attribute for counting genres
    artist_count = {}  # Class attribute for counting artists

    def __init__(self, name, artist, genre):
        self.name = name  # Instance attribute for the song name
        self.artist = artist  # Instance attribute for the artist
        self.genre = genre  # Instance attribute for the genre

        # Increment the song count
        Song.add_song_to_count()
        
        # Add the genre to the genres list
        Song.add_to_genres(genre)

        # Add the artist to the artists list
        Song.add_to_artists(artist)

        # Update genre count
        Song.add_to_genre_count(genre)

        # Update artist count
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
