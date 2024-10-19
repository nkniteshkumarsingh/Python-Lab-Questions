from functools import total_ordering


@total_ordering
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return f"<{self.__module__}.{type(self).__name__} object at {hex(id(self))}> ({self.title}, {self.author}, {self.isbn})"

    def __str__(self):
        return f"{self.title} by {self.author}; ISBN: {self.isbn}"

    def __lt__(self, other):
        return (self.author < other.author) or \
            (self.author == other.author and self.title < other.title)

    def __eq__(self, other):
        return self.author == other.author and self.title == other.title


if __name__ == "__main__":
    b = Book("Ulysses", "Joyce, James", 140920051908)
    b2 = Book("Ulysses", "Joyce, James", 140920051908)

    print(b)
    # print(b.__repr__())
    print(repr(b))
    print(f"b == b2: {b == b2}")

    d = Book("Book of Pride and Prejudice", "Austen, Jane", "N/A")

    print(f"d < b: {d < b}")
