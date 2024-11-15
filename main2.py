class Library:

    def __init__(self,list_of_books,name):
        self.bookshelf=list_of_books
        self.name=name
        self.lendDict={}

    def displayBooks(self):
        print(f"We have the following books in our library:{self.name}")
        for book in self.bookslist:
            print(book)

    def lendBook(self.booksList):
        if book no in self.booksList:
            print("Sorry, we do not have that book.")
        elif book in self.lendDict:
            print(f"The book is already being used by {self.lendDict[book]}")
        else:
            self.lendDict[book]=user
            print("Lender Book database has been updated. You can take the book now.")

    def addBook(self,book):
        self.bookList.append(book)
        print(f"{book}has been added to the book list.")

    def returnBook(self, book):
        if book in self.lendDict:
            del self.lendDict[book]
            print("Book has been returned.")
        else:
            print("THat book wasn't borrowed from us.")

if __name__=='__main__':
    books=Library(['Python','Rich Dad Poor Dad','Harry Potter','C++ Basics','Algorithms by CLRS'], "Let's Upskill")