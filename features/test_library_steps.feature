# features/test_library_steps.feature

Feature: BookService functionality

  Scenario: Add a book to the bookstore
    Given the BookService is initialized
    When a book with book_id "123" is added to the bookstore
    Then the book with book_id "123" should be in the bookstore

  Scenario: Add a user to the userstore
    Given the UserService is initialized
    When a user with user_id "12345" is added to the userstore
    Then the user with user_id "12345" should be in the userstore

  Scenario: Remove a book from the bookstore
    Given the BookService is initialized
    When a book with book_id "123" is added to the bookstore
    When the book with book_id "123" is removed from the bookstore
    Then the book with book_id "123" should not be in the bookstore

  Scenario: Remove a user from the userstore
    Given the UserService is initialized
    When a user with user_id "12345" is added to the userstore
    When the user with user_id "12345" is removed from the userstore
    Then the user with user_id "12345" should not be in the userstore

  Scenario: Search a book to the bookstore
    Given the BookService is initialized
    When book with book_id "568" and title "test-568" is added to the bookstore
    Then the book when searched with attribute "title" and term "test-568", it should match with book_id "568"

 Scenario: Add limit to total book that can be issued for user
    Given the UserService is initialized
    Given the UserSettingService is initialized
    When a user with user_id "123456" is added to the userstore
    When limit of "5" for "123456" is added to usersetting
    Then limit of "5" for user_id "123456" should be there in usersetting

  Scenario: book assigned to user
    Given the UserService is initialized
    Given the UserSettingService is initialized
    Given the BookService is initialized
    Given the UserBookStoreService is initialized
    Given the BookAssignmentService is initialized
    When user with user_id "123456" and "123457" is added to the userstore
    When book with book_id "123" and "124" and "125" and "126" and "127" and "128" is added to the bookstore
    When limit of "5" for "123456" is added to usersetting
    When limit of "2" for "123457" is added to usersetting
    When book_id "123" and book_id "124" and book_id "125" is assigned to user_id "123456" on date "2024-08-14"
    When book_id "126" and book_id "127" is assigned to user_id "123457" on date "2024-08-14"
    Then book_id "126" and book_id "127" should be assigned to user_id "123457"

   Scenario: user capacity already full
    Given the UserService is initialized
    Given the UserSettingService is initialized
    Given the BookService is initialized
    Given the UserBookStoreService is initialized
    When user with user_id "123456" and "123457" is added to the userstore
    When book with book_id "123" and "124" and "125" and "126" and "127" and "128" is added to the bookstore
    When limit of "5" for "123456" is added to usersetting
    When limit of "2" for "123457" is added to usersetting
    When book_id "123" and book_id "124" and book_id "125" is assigned to user_id "123456" on date "2024-08-14"
    When book_id "126" and book_id "127" is assigned to user_id "123457" on date "2024-08-14"
    Then should throw the exception as user capacity already full

   Scenario: user return book
    Given the UserService is initialized
    Given the UserSettingService is initialized
    Given the BookService is initialized
    Given the UserBookStoreService is initialized
    Given the BookAssignmentService is initialized
    Given the BookSettingService is initialized
    When user with user_id "123456" and "123457" is added to the userstore
    When book with book_id "123" and "124" and "125" and "126" and "127" and "128" is added to the bookstore
    When limit of "5" for "123456" is added to usersetting
    When limit of "2" for "123457" is added to usersetting
    When book with book_id "123" and "124" is assigned maximum return date as "3"
    When book with book_id "123" and "124" is assigned maximum fine as "100"
    When book_id "123" and book_id "124" and book_id "125" is assigned to user_id "123456" on date "2024-08-14"
    When user_id "123456" return book_id "123" and book_id "124" on date "2024-08-20"
    Then book_id "125" should be assigned to user_id "123456"

   Scenario: Add maximum date of return
    Given the UserService is initialized
    Given the UserSettingService is initialized
    Given the BookService is initialized
    Given the UserBookStoreService is initialized
    Given the BookAssignmentService is initialized
    Given the BookSettingService is initialized
    When book with book_id "123" and "124" is assigned maximum return date as "3"
    Then return date of "3" for book_id "123" should be there in booksetting

  Scenario: Add fine to book
    Given the UserService is initialized
    Given the UserSettingService is initialized
    Given the BookService is initialized
    Given the UserBookStoreService is initialized
    Given the BookAssignmentService is initialized
    Given the BookSettingService is initialized
    When book with book_id "123" and "124" is assigned maximum fine as "100"
    Then book with book_id "123" should be assigned maximum fine as "100"

  Scenario: check total fine
    Given the UserSettingService is initialized
    Given the BookSettingService is initialized
    Given the UserService is initialized
    Given the BookService is initialized
    Given the UserBookStoreService is initialized
    Given the BookAssignmentService is initialized
    When user with user_id "123456" and "123457" is added to the userstore
    When book with book_id "123" and "124" and "125" and "126" and "127" and "128" is added to the bookstore
    When book_id "123" and book_id "124" and book_id "125" is assigned to user_id "123456" on date "2024-08-14"
    Then fine of "300" should be on user_id "123456" for book_id "123" for return_date "2024-08-20"



  # Add more scenarios for other functionalities (assign, return, search) if needed
