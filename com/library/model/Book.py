# Book
#
# {
#   "book_id": 1,
#   "title": "The Great Gatsby",
#   "author": "F. Scott Fitzgerald",
#   "isbn": "978-3-16-148410-0"
# }

class Book:
    def __init__(self, book_id, title, author, isbn, category, groupid):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.category = category
        self.groupid = groupid