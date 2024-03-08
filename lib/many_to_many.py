class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)


class Book:

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)


class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self._author = author
        self._book = book
        self._date = date
        self._royalties = royalties

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception
        
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if isinstance(book, Author):
            self._book = book
        else:
            raise Exception
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise Exception
        self._date = date

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalty):
        if not isinstance (royalty, int):
            raise Exception
        self._royalties = royalty
        