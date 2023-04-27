# Wikipedia Data Scraping
**This is a Python personal project script that scrapes data from the "List of book titles taken from literature" Wikipedia page and stores it in a SQLite database. The script uses the BeautifulSoup library to parse the HTML code of the page and extract the relevant data, which includes the title, author, and literary reference of each book. The book data is then inserted into a database table called "books" using parameterized SQL queries.**

## Requirements:
*To run this script, you need to have the following module:*
- BeautifulSoup 4.x
- Requests 2.x
- SQLite 3.x

## Installation
```
pip install BeautifulSoup4
pip install requests
pip install sqlite3
```

## Procedure
he script works in the following way:
1. The target URL is defined.
2. The HTML code of the website is obtained using requests.get() method and stored in a variable called html_code.
3. A BeautifulSoup object called soup is created for web scraping.
4. The target component (a table with class 'wikitable sortable') is identified using the find() method of BeautifulSoup and stored in a variable called table.
5. All table rows in the table are identified using the find_all() method of BeautifulSoup and stored in a variable called table_rows.
6. The title of the table row is scraped to make a table row in the database.
7. The book data (title, author, and literary reference) is scraped and stored in a list called books.
8. A database is created and the books information is stored in it using sqlite. A connection to the database is made using sqlite.connect(), a cursor object is created using the cursor() method, and the books are inserted into the database using cursor.execute() method.
9. If a book cannot be inserted into the database due to an error, the error message is printed.

## Functions and Variables
The script uses the following functions and variables:

- requests.get(): Used to obtain the HTML code of a website
- BeautifulSoup(): Used to create a BeautifulSoup object for web scraping
- table.find(): Used to find the target component (table with class 'wikitable sortable')
- table.find_all(): Used to find all table rows in the target table
- split(): Used to split a string into a list of strings using a delimiter
- tuple(): Used to create a tuple from a list
- sqlite.connect(): Used to create a connection to a SQLite database
- cursor(): Used to create a cursor object for executing SQL commands
- cursor.execute(): Used to execute an SQL command
- conn.commit(): Used to commit changes to the database
- cursor.close(): Used to close the cursor object
- conn.close(): Used to close the connection to the database
- url: A string variable containing the target URL
- html_code: A string variable containing the HTML code of the website
- soup: A BeautifulSoup object for web scraping
- table: A BeautifulSoup object containing the target table
- table_rows: A list containing all table rows in the target table
- title_row: A tuple containing the title of the table row
- books: A list containing tuples of book data (title, author, and literary reference)
- conn: A SQLite database connection object
- cursor: A cursor object for executing SQL commands on the database.

## Acknowledgments
Thanks to the creators of BeautifulSoup, Requests, and SQLite for providing the tools used in this project.