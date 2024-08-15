from com.library.service.UserBookStoreService import UserBookStoreService
from com.library.service.UserSettingService import UserSettingService
from com.library.store.BookStore import BookStore


class BookService:

    def __init__(self):
        self.bookStore = BookStore()
        self.userBookStoreService = UserBookStoreService()
        self.userSettingService = UserSettingService()

    def addBook(self, bookList):
        return self.bookStore.addBook(bookList)

    def removeBook(self, book):
        return self.bookStore.removeBook(book)

    def getBook(self, book):
        return self.bookStore.getBook(book)

    def assignBook(self, bookList, userId):
        self.userBookStoreService.assignBookToUser(bookList, userId)

    def returnBook(self, bookIdList, userId, returnDate):
        self.userBookStoreService.returnBook(bookIdList, userId, returnDate)

    def searchBook(self, searchKey, searchItem):
        return self.bookStore.searchBook(searchKey, searchItem)
