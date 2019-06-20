class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


class yeah(object):

    def __init__(self, words):
        self.words = words

    def say_the_words(self):
        for word in self.words:
            print(word)

my_word = yeah(["hei you are a good boy",
                "best wish to you."])

my_word.say_the_words()
