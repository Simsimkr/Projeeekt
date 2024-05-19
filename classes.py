from random import choice
import uuid


class Book:
    def __init__(self, name, autor, styl, dlugosc, rok):
        self.name = str(name)
        self.dlugosc = str(dlugosc)
        self.styl = str(styl)
        self.rok = str(rok)
        self.autor = str(autor)
        self.id = str(uuid.uuid4())

    def infb(self):
        print(f"Nazwa = {self.name}")
        print(f"Autor = {self.autor}")
        print(f"Styl = {self.styl}")
        print(f"Dlugosc = {self.dlugosc} str.")
        print(f"Rok wydania = {self.rok}r.")
        print(f"Id = {self.id}")


class Library:
    l = 0

    def __init__(self):
        self.numer = Library.l
        Library.l += 1
        self.books = []

    def add_book(self, b):
        self.books.append(b)

    def remove_book(self, b):
        for el in self.books:
            if b.name == el.name and b.autor == el.autor and b.styl == el.styl and b.dlugosc == el.dlugosc and b.rok == el.rok and b.id == el.id:
                self.books.remove(el)

    def infl(self):
        print(self.numer)
        for el in self.books:
            print(el.infb())
            print("+" * 80)


class Men:
    def __init__(self, book):
        self.book = book
        self.marzenia = self.gen_marzenia()

    def inf(self):
        print(self.marzenia)
        print(self.book.infb())

    def gen_marzenia(self):
        l = []
        b = ['nazwa', 'dlugosc', 'styl', 'rok', 'autor']
        for i in range(2):
            a = choice(b)
            if a == "nazwa":
                l.append('nazwa')
                l.append(self.book.name)
            elif a == "autor":
                l.append('autor')
                l.append(self.book.autor)
            elif a == "styl":
                l.append('styl')
                l.append(self.book.styl)
            elif a == "dlugosc":
                l.append('dlugosc')
                l.append(self.book.dlugosc)
            elif a == "rok":
                l.append('rok')
                l.append(self.book.rok)
            b.remove(a)
        return l

    def test(self, b):
        i = 0
        a = 0

        if b.name == self.book.name and b.autor == self.book.autor and b.styl == self.book.styl and b.dlugosc == self.book.dlugosc and b.rok == self.book.rok and b.id == self.book.id:
            print("idealna ksianzka")
            return 20

        while i < 2 and a < 4:
            if self.marzenia[0 + a] == "nazwa":
                if self.marzenia[1 + a] == b.name:
                    print("ok")
                    i += 1
            elif self.marzenia[0 + a] == "autor":
                if self.marzenia[1 + a] == b.autor:
                    print("ok")
                    i += 1
            elif self.marzenia[0 + a] == "styl":
                if self.marzenia[1 + a] == b.styl:
                    print("ok")
                    i += 1
            elif self.marzenia[0 + a] == "dlugosc":
                if self.marzenia[1 + a] == b.dlugosc:
                    print("ok")
                    i += 1
            elif self.marzenia[0 + a] == "rok":
                if self.marzenia[1 + a] == b.rok:
                    print("ok")
                    i += 1
            elif self.marzenia[0 + a] == "id":
                if self.marzenia[1 + a] == b.id:
                    print("ok")
                    i += 1
            a += 2
            if i == 2:
                return 10
            elif i == 1:
                return 5
            elif i == 0:
                return 0
