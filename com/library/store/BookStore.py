class BookStore:

    def __init__(self):
        self.bookstore = {}

    def addBook(self, bookList):
        for book in bookList:
            self.bookstore[book.book_id] = book
        return True

    def getBooks(self):
        return self.bookstore

    def getBook(self, book):
        if book.book_id in self.bookstore:
            return True
        return False
    def removeBook(self, book):
        del self.bookstore[book.book_id]
        return True

    def searchBook(self, searchKey, searchItem):
        filteredObjects = []
        for item in self.bookstore.values():
            if getattr(item, searchKey) == searchItem:
                filteredObjects.append(item)
        return filteredObjects