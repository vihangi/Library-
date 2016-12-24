
"""

Reading List 1.0 - by Lindsay Ward
4 books loaded from books.csv
Menu:
R - List required books
C - List completed books
A - Add new book
M - Mark a book as completed
Q - Quit
r
Required books:
 0. Developing the Leader Within You         by John Maxwell         225 pages
 1. The 360 Degree Leader                    by John Maxwell         369 pages
 3. The Practice of Computing Using Python   by Punch and Enbody     792 pages
Total pages for 3 books: 1386
"""
from operator import itemgetter
FILENAME = "books.csv"
file_list = []

def print_header():
    print("""
Reading List 1.0 - by Yok Yen
{} books loaded from books.csv
    """)

def read_file():
    global file_list
    file_pointer= open(FILENAME, "r")
    for index, data in enumerate(file_pointer.readlines()):
        data = data.strip()
        datum = data.split(",")
        print(index, datum)
        file_list.append(datum)
    file_list.sort(key=itemgetter(1, 2))
    print(file_list)
    file_pointer.close()

read_file()

