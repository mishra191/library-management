from com.library.exception.BookNotFound import BookNotFound
from com.library.exception.UserNotFound import UserNotFound


class BookAssignmentStore:

    def __init__(self):
        self.booktoassignmentmapping = {}

    def setDateToBook(self, book, date):
        self.booktoassignmentmapping[book.book_id] = date

    def getDateToBook(self, bookId):
        return self.booktoassignmentmapping[bookId]

    def removeDateToBook(self, bookIdList):
        for bookId in bookIdList:
            del self.booktoassignmentmapping[bookId]




