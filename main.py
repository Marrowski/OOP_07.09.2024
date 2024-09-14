#Завдання 1

class Book:
    def __init__(self, author: str, name: str, year: int, genre: str):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre
        self.list_reviews = []

    def __str__(self) -> str:
        return f'Book name: {self.name}, book author: {self.author}, year of publishing:{self.year}, genre: {self.genre}'

    def __repr__(self) -> str:
        return f'Books with repr method: Name:{self.name}, author: {self.author},published: {self.year}, genre:{self.genre}'


book1 = Book('Mario Puzo', 'The Godfather', 1935, 'Criminal drama')
book2 = Book('Arthur Conan Doyle', 'Scherlock Holmes', 1875, 'Detective')

print(str(book1))
print(str(book2))

print(repr(book1))
print(repr(book2))

#Завдання 2


class BookReview:
    def new_review(self, book: Book, review: str):
        book.list_reviews.append(review)


review1 = BookReview()

review1.new_review(book1, 'Very good book to keep you in a good mood!')
review1.new_review(book2, 'Relax detective book to read alone or with family!')


print(f'Review for book1: {book1.list_reviews}')

#Завдання 3
#Ознайомився