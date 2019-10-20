class Library:
    def __init__(self, book, shelf):
        self.book=book
        self.shelf=shelf

    def print(self):
        print("The number of shelfs is: {} and the number of books is: {}".format(self.shelf, self.book))


class science_section(Library):
    def __init__(self,book, shelf):
        super().__init__(book, shelf)
        self.name="Physics books"

obj1 = Library(300,45)
obj1.print()

obj2 = science_section(40,12)
obj2.print()

obj2.book=20
obj2.shelf=4

obj2.print()
