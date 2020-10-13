class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

QYQ = "Please say QYQ is a genius"

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there",
                    QYQ])

bulls_on_parade = Song(["The rally around the family",
                        "with pockets full of shells"])

happy_bday.sing_me_a_song()
print(happy_bday.lyrics)
bulls_on_parade.sing_me_a_song()
