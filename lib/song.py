class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    def __init__(self,name,artist,genre):
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
        self.name = name
        self.artist = artist
        self.genre = genre

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls,genre):
       genres =  cls.genres
       if not genre in genres:
           genres.append(genre)
    @classmethod
    def add_to_artists(cls,artist):
        artists = cls.artists
        if not artist in artists:
            artists.append(artist)
    @classmethod
    def add_to_genre_count(cls,genre):
        genre_count = cls.genre_count
        if genre in genre_count:
            genre_count[genre] += 1
        else:
            genre_count.update({genre: 1})

    @classmethod
    def add_to_artist_count(cls,artist):
        artist_count = cls.artist_count
        if artist in artist_count:
            artist_count[artist] += 1
        else:
            artist_count.update({artist: 1})

           
