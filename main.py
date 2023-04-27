# Importing required libraries
from bs4 import BeautifulSoup
import requests
import sqlite3

# Target URL to scrape data from
url = "https://en.wikipedia.org/wiki/List_of_book_titles_taken_from_literature"

# Get the HTML code of the website
html_code = requests.get(url).text

# Create a BeautifulSoup object for web scraping
soup = BeautifulSoup(html_code, 'lxml')

# Find a table that has a class of 'wikitable sortable'
table = soup.find('table', class_ = "wikitable sortable")

# Find all table rows in the table
table_rows = table.find_all('tr')

# Extract the title of the table row
title_row = tuple(table_rows[0].text.strip().split('\n')[1:-1])

# Extract book data (title, author, and literary reference) and store it in a list called 'books'
books = [tuple(book_data.text.strip().split('\n')[1:-1]) for book_data in table_rows[1:]]

# Create a connection to the database
conn = sqlite3.connect('books.db')

# Create a cursor object for executing SQL commands
cursor = conn.cursor()

# Execute parameterized SQL queries to insert book data into the database
for book in books:
    try:
        cursor.execute("INSERT INTO books (title, author, reference) VALUES (?, ?, ?)", book)
        print("Successfully inserted book")
    except sqlite3.Error as e:
        print("Failed inserting book :", e)

# Commit changes to the database
conn.commit()

# Close the cursor and connection to the database
cursor.close()
conn.close()
