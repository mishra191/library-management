from com.library.exception.BookNotFound import BookNotFound
from com.library.exception.UserNotFound import UserNotFound


class UserBookStore:

    def __init__(self):
        self.usertobookmapping = {}
        self.booktousermapping = {}

    def assignBookToUser(self, bookList, userid):
        if userid not in self.usertobookmapping:
            self.usertobookmapping[userid] = []
        self.usertobookmapping[userid].extend(bookList)
        for book in bookList:
            self.booktousermapping[book.book_id] = userid

    def returnBook(self, bookIdList, userId):
        booklistOriginal = [book for book in self.usertobookmapping[userId] if book.book_id not in bookIdList]
        self.usertobookmapping[userId] = booklistOriginal
        for bookId in bookIdList:
            del self.booktousermapping[bookId]

    def getTotalBookAssignedToUser(self, userId):
        if userId not in self.usertobookmapping:
            return 0
        return len(self.usertobookmapping[userId])

    def getAssignedBook(self, userId):
        return self.usertobookmapping[userId]
