#OOP

#properties + functions
#class template

#book tittle,author, isbn, price

class Book:
    #constructor==functions(special function used to set up the book)
    # constructor used to build object
    def __init__(self, title, author, isbn, price):
        self.title =title
        self.author = author
        self.isbn = isbn
        self.price = price
    def print_details(self):
        print("Title", self.title)
        print("Author:", self.author)
        print("price:", self.price)
        print("---------------------")

    def apply_discount(self, discount ):
        self.price= self.price*(1-discount/100)
        print("New price is", self.price)
b1 = Book("Two rivers", "chinua Achebe","ISB001", 300)
b2 = Book("Think and Grow big", "John Moore", "ISB002", 700)

b1.print_details()

b1.apply_discount(10)







