from com.library.store.BookSettingStore import BookSettingStore


class BookSettingService:

    def __init__(self):
        self.bookSettingStore = BookSettingStore()

    def setBookReturnDatePerBook(self, bookidList, date):
        self.bookSettingStore.setBookReturnDatePerBook(bookidList, date);

    def getBookReturnDatePerBook(self, book_id):
        return self.bookSettingStore.getBookReturnDatePerBook(book_id)

    def setBookFinePerBook(self, bookidList, perDayFine):
        self.bookSettingStore.setBookFinePerBook(bookidList, perDayFine)

    def getBookFinePerBook(self, book_id):
        return self.bookSettingStore.getBookFinePerBook(book_id)