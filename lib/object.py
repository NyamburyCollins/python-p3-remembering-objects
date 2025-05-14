class Song:

    all = [] #an attribute can store all instances of a song class

    def __init__(self, name): #instances of a class
        self.name = name
        Song.add_song_to_all(self)

    @classmethod
    def add_song_to_all(cls, song):
        cls.all.append(song)

    @classmethod
    def show_song_names(cls):
        print([song.name for song in cls.all])

ninety_nine_problems = Song("99 Problems")
thriller = Song("Thriller")
Song.show_song_names()
# => ['99 Problems', 'Thriller']

# Self new object that have been created which is a method scope
# _init_ instance method