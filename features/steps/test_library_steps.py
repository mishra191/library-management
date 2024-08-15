# features/steps/test_library_steps.py

from behave import given, when, then
from com.library.model.Book import Book
from com.library.model.User import User
from com.library.service.BookAssignmentService import BookAssignmentService
from com.library.service.BookService import BookService
from com.library.service.BookSettingService import BookSettingService
from com.library.service.UserBookStoreService import UserBookStoreService
from com.library.service.UserService import UserService
from com.library.service.UserSettingService import UserSettingService
from com.library.exception.UserCapacityAlreadyFull import UserCapacityAlreadyFull


@given('the BookService is initialized')
def initialize_book_service(context):
    context.book_service = BookService()


@given('the UserService is initialized')
def initialize_user_service(context):
    context.user_service = UserService()


@given('the UserSettingService is initialized')
def initialize_user_setting_service(context):
    context.user_setting_service = UserSettingService()


@given('the BookSettingService is initialized')
def initialize_book_setting_service(context):
    context.book_setting_service = BookSettingService()


@given('the UserBookStoreService is initialized')
def initialize_user_service(context):
    context.user_book_store_service = UserBookStoreService()


@given('the BookAssignmentService is initialized')
def initialize_book_assignment_service(context):
    context.book_assignment_service = BookAssignmentService()


@when('a user with user_id "{user_id}" is added to the userstore')
def add_user_to_userstore(context, user_id):
    userList = []
    user = User(user_id, "firstName", "lastName", "address")
    userList.append(user)
    context.user_service.addUser(userList)


@when('limit of "{limit}" for "{user_id}" is added to usersetting')
def add_limit_to_usersetting(context, limit, user_id):
    context.user_setting_service.setBookLimitPerUser(user_id, int(limit))


@when('a user with user_id "{user_id}" is removed from the userstore')
def remove_user_from_userstore(context, user_id):
    user = User(user_id, "firstName", "lastName", "address")
    context.user_service.removeUser(user)


@when('a book with book_id "{book_id}" is added to the bookstore')
def add_book_to_bookstore(context, book_id):
    bookList = []
    book = Book(book_id, "TestTitle", "TestAuthor", "TestISBN", "TestCategory", "22")
    bookList.append(book)
    context.book_service.addBook(bookList)


@when('book with book_id "{book_id}" and title "{title}" is added to the bookstore')
def add_book_to_bookstore_with_title(context, book_id, title):
    bookList = []
    book = Book(book_id, title, "TestAuthor", "TestISBN", "TestCategory", "22")
    bookList.append(book)
    context.book_service.addBook(bookList)


@then('the book with book_id "{book_id}" should be in the bookstore')
def verify_book_in_bookstore(context, book_id):
    book = Book(book_id, "TestTitle", "TestAuthor", "TestISBN", "TestCategory", "22")
    assert context.book_service.getBook(book) is True


@then('the user with user_id "{user_id}" should be in the userstore')
def verify_user_in_userstore(context, user_id):
    user = User(user_id, "firstName", "lastName", "address")
    assert context.user_service.getUser(user) is True


@then('the user with user_id "{user_id}" should not be in the userstore')
def verify_user_not_in_userstore(context, user_id):
    user = User(user_id, "firstName", "lastName", "address")
    assert context.user_service.getUser(user) is False


@when('the book with book_id "{book_id}" is removed from the bookstore')
def remove_book_from_bookstore(context, book_id):
    book = Book(book_id, "TestTitle", "TestAuthor", "TestISBN", "TestCategory", "22")
    context.book_service.removeBook(book)


@when('the user with user_id "{user_id}" is removed from the userstore')
def remove_user_from_bookstore(context, user_id):
    user = User(user_id, "firstName", "lastName", "address")
    context.user_service.removeUser(user)


@then('the book when searched with attribute "{attribute}" and term "{term}", it should match with book_id "{book_id}"')
def verify_book_in_bookstore_with_attribute(context, attribute, term, book_id):
    book = context.book_service.searchBook(attribute, term)[0]
    assert book.book_id == book_id, f"Assertion Error: Expected {book_id}, but got {book.book_id}"


@then('the book with book_id "{book_id}" should not be in the bookstore')
def verify_book_not_in_bookstore(context, book_id):
    book = Book(book_id, "TestTitle", "TestAuthor", "TestISBN", "TestCategory", "22")
    assert context.book_service.getBook(book) is False


@then('limit of "{limit}" for user_id "{user_id}" should be there in usersetting')
def verify_limit_for_user(context, limit, user_id):
    assert context.user_setting_service.getBookLimitPerUser(user_id) == int(limit)


@when('user with user_id "{user_id_1}" and "{user_id_2}" is added to the userstore')
def add_multiple_user(context, user_id_1, user_id_2):
    userList = []
    user1 = User(user_id_1, "firstName", "lastName", "address")
    user2 = User(user_id_2, "firstName", "lastName", "address")
    userList.append(user1)
    userList.append(user2)
    context.user_service.addUser(userList)


@when(
    'book with book_id "{book_id_1}" and "{book_id_2}" and "{book_id_3}" and "{book_id_4}" and "{book_id_5}" and "{book_id_6}" is added to the bookstore')
def add_multiple_books(context, book_id_1, book_id_2, book_id_3, book_id_4, book_id_5, book_id_6):
    bookList = []
    book1 = Book(book_id_1, "title", "TestAuthor", "TestISBN", "TestCategory", "22")
    book2 = Book(book_id_2, "title", "TestAuthor", "TestISBN", "TestCategory", "22")
    book3 = Book(book_id_3, "title", "TestAuthor", "TestISBN", "TestCategory", "22")
    book4 = Book(book_id_4, "title", "TestAuthor", "TestISBN", "TestCategory", "22")
    book5 = Book(book_id_5, "title", "TestAuthor", "TestISBN", "TestCategory", "22")
    book6 = Book(book_id_6, "title", "TestAuthor", "TestISBN", "TestCategory", "22")
    bookList.append(book1)
    bookList.append(book2)
    bookList.append(book3)
    bookList.append(book4)
    bookList.append(book5)
    bookList.append(book6)
    context.book_service.addBook(bookList)


@when('book_id "{book_id_1}" and book_id "{book_id_2}" and book_id "{book_id_3}" is assigned to user_id "{user_id}" '
      'on date "{assigned_date}"')
def assignThreeBooks(context, book_id_1, book_id_2, book_id_3, user_id, assigned_date):
    bookList = []
    book1 = Book(book_id_1, "title", "TestAuthor", "TestISBN", "TestCategory", "22")
    book2 = Book(book_id_2, "title", "TestAuthor", "TestISBN", "TestCategory", "22")
    book3 = Book(book_id_3, "title", "TestAuthor", "TestISBN", "TestCategory", "22")
    bookList.append(book1)
    bookList.append(book2)
    bookList.append(book3)
    context.user_book_store_service.assignBookToUser(bookList, user_id, assigned_date)


@when('book_id "{book_id_1}" and book_id "{book_id_2}" is assigned to user_id "{user_id}" on date "{assigned_date}"')
def assignTwoBooks(context, book_id_1, book_id_2, user_id, assigned_date):
    bookList = []
    book1 = Book(book_id_1, "title", "TestAuthor", "TestISBN", "TestCategory", "22")
    book2 = Book(book_id_2, "title", "TestAuthor", "TestISBN", "TestCategory", "22")
    bookList.append(book1)
    bookList.append(book2)
    context.user_book_store_service.assignBookToUser(bookList, user_id, assigned_date)


@then('book_id "{book_id_1}" and book_id "{book_id_2}" should be assigned to user_id "{user_id}"')
def getAssignedBooks(context, book_id_1, book_id_2, user_id):
    bookList = []
    book1 = Book(book_id_1, "title", "TestAuthor", "TestISBN", "TestCategory", "22")
    book2 = Book(book_id_2, "title", "TestAuthor", "TestISBN", "TestCategory", "22")

    bookList.append(book1)
    bookList.append(book2)

    assignedBookList = context.user_book_store_service.getAssignedBooks(user_id)
    assert len(assignedBookList) == len(bookList)

    # Check if all book_ids in assigned_books match those in expected_books
    expected_ids = sorted([book.book_id for book in bookList])
    assigned_ids = sorted([book.book_id for book in assignedBookList])

    assert expected_ids == assigned_ids, (
        f"Expected book IDs {expected_ids} but found {assigned_ids}"
    )


@then('should throw the exception as user capacity already full')
def check_user_capacity_full_exception(context):
    try:
        # This step is expected to raise an exception
        context.user_book_store_service.assignBookToUser(
            [Book("128", "title", "TestAuthor", "TestISBN", "TestCategory", "22")], "123457", "2024-08-14")
        assert False, "Expected UserCapacityAlreadyFull exception, but none was raised."
    except UserCapacityAlreadyFull as e:
        assert str(e) == "user capacity already full", (
            f"Expected error message 'user capacity already full', but got '{str(e)}'"
        )


@when('user_id "{user_id}" return book_id "{book_id_1}" and book_id "{book_id_2}" on date "{return_date}"')
def user_return_book(context, user_id, book_id_1, book_id_2, return_date):
    bookIdList = []
    bookIdList.append(book_id_1)
    bookIdList.append(book_id_2)
    context.user_book_store_service.returnBook(bookIdList, user_id, return_date)


@then('book_id "{book_id_1}" should be assigned to user_id "{user_id}"')
def getAssignedBooksForReturn(context, book_id_1, user_id):
    bookList = []
    book1 = Book(book_id_1, "title", "TestAuthor", "TestISBN", "TestCategory", "22")
    bookList.append(book1)
    assignedBookList = context.user_book_store_service.getAssignedBooks(user_id)

    assert len(assignedBookList) == len(bookList)

    # Check if all book_ids in assigned_books match those in expected_books
    expected_ids = sorted([book.book_id for book in bookList])
    assigned_ids = sorted([book.book_id for book in assignedBookList])

    assert expected_ids == assigned_ids, (
        f"Expected book IDs {expected_ids} but found {assigned_ids}"
    )


@when('book with book_id "{book_id_1}" and "{book_id_2}" is assigned maximum return date as "{returnDate}"')
def maximum_return_date(context, book_id_1, book_id_2, returnDate):
    bookIdList = []
    bookIdList.append(book_id_1)
    bookIdList.append(book_id_2)
    context.book_setting_service.setBookReturnDatePerBook(bookIdList, returnDate)


@when('book with book_id "{book_id_1}" and "{book_id_2}" is assigned maximum fine as "{fine}"')
def maximum_return_date(context, book_id_1, book_id_2, fine):
    bookIdList = []
    bookIdList.append(book_id_1)
    bookIdList.append(book_id_2)
    context.book_setting_service.setBookFinePerBook(bookIdList, fine)


@then('return date of "{return_date}" for book_id "{book_id}" should be there in booksetting')
def checkMaximumReturnDate(context, return_date, book_id):
    setting_return_date = context.book_setting_service.getBookReturnDatePerBook(book_id)
    assert setting_return_date == return_date


@then('book with book_id "{book_id}" should be assigned maximum fine as "{fine}"')
def checkMaximumFine(context, book_id, fine):
    setting_maximum_fine = context.book_setting_service.getBookFinePerBook(book_id)
    assert setting_maximum_fine == fine


@then('fine of "{fine}" should be on user_id "{user_id}" for book_id "{book_id}" for return_date "{return_date}"')
def user_return_book_with_fine(context, fine, user_id, book_id, return_date):
    bookIdList = []
    bookIdList.append(book_id)
    context.user_book_store_service.setBookFinePerBook(bookIdList, "100")
    context.user_book_store_service.setBookReturnDatePerBook(bookIdList, "3")
    fine_dict = context.user_book_store_service.returnBook(bookIdList, user_id, return_date)
    total_fine = fine_dict[book_id]
    assert int(total_fine) == int(fine)