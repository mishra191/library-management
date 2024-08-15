from com.library.exception.UserCapacityAlreadyFull import UserCapacityAlreadyFull
from com.library.service.BookAssignmentService import BookAssignmentService
from com.library.service.BookSettingService import BookSettingService
from com.library.service.UserSettingService import UserSettingService
from com.library.store.UserBookStore import UserBookStore
from datetime import datetime


class UserBookStoreService:

    def __init__(self):
        self.userBookStore = UserBookStore()
        self.userSettingService = UserSettingService()
        self.bookSettingService = BookSettingService()
        self.bookAssignmentService = BookAssignmentService()

    def assignBookToUser(self, bookList, userid, assignmentDate):
        totalBookLimit = self.userSettingService.getBookLimitPerUser(userid)
        alreadyAssignedBook = self.userBookStore.getTotalBookAssignedToUser(userid)
        if alreadyAssignedBook + len(bookList) > totalBookLimit:
            raise UserCapacityAlreadyFull("user capacity already full")
        self.userBookStore.assignBookToUser(bookList, userid)
        self.bookAssignmentService.setDateToBook(bookList, assignmentDate)

    def getAssignedBooks(self, userid):
        return self.userBookStore.getAssignedBook(userid)

    def checkFineForBook(self, bookId, returnDate, fine):
        assignedDate = self.bookAssignmentService.getDateToBook(bookId)

        # Convert strings to datetime objects
        date_1 = datetime.strptime(assignedDate, "%Y-%m-%d")
        date_2 = datetime.strptime(returnDate, "%Y-%m-%d")

        # Calculate the difference
        difference = date_2 - date_1

        # Get the difference in days
        days_difference = difference.days

        maximumDay = int(self.bookSettingService.getBookReturnDatePerBook(bookId))

        if maximumDay != -1 and maximumDay < days_difference:
            totalFine = int(self.bookSettingService.getBookFinePerBook(bookId))
            fine[bookId] = int((days_difference - maximumDay)) * totalFine

    def returnBook(self, bookIdList, userId, returnDate):
        fine = {}
        self.userBookStore.returnBook(bookIdList, userId)
        for bookId in bookIdList:
            self.checkFineForBook(bookId, returnDate, fine)
        self.bookAssignmentService.removeDateToBook(bookIdList)
        return fine

    def setBookFinePerBook(self, bookIdList, fine):
        self.bookSettingService.setBookFinePerBook(bookIdList, fine)
    def setBookReturnDatePerBook(self, bookIdList, maximumReturnDate):
        self.bookSettingService.setBookReturnDatePerBook(bookIdList, maximumReturnDate)
