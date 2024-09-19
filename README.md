# db-basics
## Overview
This project provides a database system that stores information about Books and Authors. 
<br> The database allows users to query various statistics, such as the youngest author, 
<br> the book with the most pages, authors without books, and the top authors who have written more than three books. 
<br> The database adheres to SOLID principles and utilizes design patterns to ensure clean, maintainable code.

## Features
* Book and Author Storage: 
  * Stores information about books, such as the title, author, year of publication, number of pages, genre, and book ID. 
  * Stores information about authors, including their name, birth year, birth place, and author ID. 

* Data Population:
  * Automatically generates 500 authors and 1000 books and populates the database.
* Queries:
  * Find the youngest author.
  * Find the book with the most pages.
  * Calculate the average number of pages for all books.
  * Find authors who have no books in the database.
  * Identify the top 5 authors who have written more than 3 books.
* Design Patterns and SOLID Principles
  * Repository Pattern:
    * Separates data access logic for authors and books into dedicated repository classes.
  * Service Layer:
    * The LibraryService class handles all the business logic and coordinates interaction between repositories and external data.
  * Single Responsibility Principle (SRP):
    * Each class has a single responsibility (e.g., AuthorRepository is responsible only for author data operations).
  * Open/Closed Principle (OCP):
    * New functionality can be added (e.g., new query types) without modifying existing code.
  * Dependency Injection:
    * The LibraryService class depends on repositories injected via the constructor, making it easy to swap implementations.
## Requirements
* Python 3.x
* SQLite (or any other supported SQL database)
* Libraries:
  * sqlite3 (for database management)
  * random (for generating test data)
  * faker (for fake data)

## Example Output
When you run the script, you can expect output like the following:
`````
Youngest Author:
     Theodore Carney
Authors with no books:
     Ruben Carroll
     Eric Harris
     Benjamin Brown
     Deborah Buckley
     ...
   
Average number of pages:
     808.08
Book with most pages:
       Book id: 21e3ea0a-b723-4483-a7e9-b017c16a0c67, name: Face his read., publishing year: 1949, author_id: c69da010-855a-41a1-aa83-a7539d075362, genre: Non-fiction, number of pages: 1497
5 Author(s) with more than 3 book(s):
     Lisa Allen with 6 book(s)
     Nathaniel Harrison with 6 book(s)
     James Simpson with 6 book(s)
     Heidi Hernandez with 6 book(s)
     Marie Schmidt with 6 book(s)
`````