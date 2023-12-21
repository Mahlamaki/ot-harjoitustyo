"Luokka yksittäiselle kirjalle"


class Book:
    "Luokka yksittäiselle kirjalle, kirja-olio"

    def __init__(self, key, title, author, rating):
        self.key = key
        self.title = title
        self.author = author
        self.rating = rating
