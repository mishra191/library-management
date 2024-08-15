class BookSettingStore:

    def __init__(self):
       self.bookReturnDate = {}
       self.bookFinePerDay = {}

    def setBookReturnDatePerBook(self, bookidList, date):
        for bookId in bookidList:
            self.bookReturnDate[bookId] = date

    def getBookReturnDatePerBook(self, book_id):

        if book_id not in self.bookReturnDate:
            return -1
        return self.bookReturnDate[book_id]

    def setBookFinePerBook(self, bookidList, perDayFine):
        for bookId in bookidList:
            self.bookFinePerDay[bookId] = perDayFine

    def getBookFinePerBook(self, book_id):
        return self.bookFinePerDay[book_id]

