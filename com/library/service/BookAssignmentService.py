
from com.library.store.BookAssignmentStore import BookAssignmentStore


class BookAssignmentService:

    def __init__(self):
        self.bookAssignmentStore = BookAssignmentStore()

    def setDateToBook(self, bookList, assignedDate):
        for book in bookList:
            self.bookAssignmentStore.setDateToBook(book, assignedDate)

    def getDateToBook(self, bookId):
        return self.bookAssignmentStore.getDateToBook(bookId)

    def removeDateToBook(self, bookList):
        return self.bookAssignmentStore.removeDateToBook(bookList)