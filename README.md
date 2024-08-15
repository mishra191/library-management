# library-management
This repository contains a Python-based Library Management System, utilizing Behavior-Driven Development (BDD) with the Behave framework. 
The system includes various services to manage books, users, and their interactions, ensuring efficient library operations.

Key Features:
Book Management:

Add/Remove Books: Books can be added to or removed from the bookstore.
Search Books: Books can be searched by specific attributes such as title.
Book Settings: The system allows setting maximum return dates and fines for overdue books.
User Management:

Add/Remove Users: Users can be added to or removed from the user store.
User Limits: Define and enforce limits on the number of books a user can borrow.
Book Assignment:

Assign Books to Users: Books can be assigned to users, respecting the borrowing limits.
Return Books: Users can return borrowed books, with fines applied for late returns.
User Capacity Management: Ensures that users do not exceed their borrowing capacity.
Fines Management:

Assign Fines: Assign fines to users based on overdue books.
Check Total Fines: Calculate and display the total fines a user owes.
Test Scenarios:
The system has been tested through several scenarios to ensure the proper functioning of each feature, including:

Adding and removing books and users.
Assigning and returning books with limits.
Managing fines and return dates.
This repository provides a robust foundation for a Library Management System, with extensive testing to cover various operational scenarios.


