

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
required_books=[]
add_books=[]
completed_books =[]
marked_books=[]
def print_header():
    print("""
Reading List 1.0 - by Yok Yen
{} books loaded from books.csv
    """)

def read_file():
    global required_books
    global completed_books
    file_pointer= open(FILENAME, "r")
    for index, data in enumerate(file_pointer.readlines()):
        data = data.strip()
        datum = data.split(",")
        #print(index, datum)

        if datum[3] == "r":
            required_books.append(datum)
        if datum[3] == "c":
           completed_books.append(datum)

    file_pointer.close()

def display_menu(menu_choice):
    """
    The display_menu function is used to display the menu and checks whether the entered menu choice is valid
    :param menu_choice: stores the menu_choice entered by the user
    :return: returns the menu choice of the user
    """
    menu_choice=menu_choice.lower
    while not (menu_choice== "r" or menu_choice=="c" or menu_choice== "a" or menu_choice== "m" or menu_choice== "q"):
        if menu_choice == "":
            print("Invalid menu choice")
            print("""Reading List 1.0 - by Vihangi Vagal
                   4 books loaded from {}
                   Menu:
                   R - List required books
                   C - List completed books
                   A - Add new book
                   M - Mark a book as completed
                   Q - Quit
                   """.format(FILENAME))
            menu_choice = input(">>>")
            menu_choice = menu_choice.lower()
            continue
        print("Invalid menu choice")
        print("""Reading List 1.0 - by Vihangi Vagal
        4 books loaded from {}
        Menu:
        R - List required books
        C - List completed books
        A - Add new book
        M - Mark a book as completed
        Q - Quit
        """.format(FILENAME))
        menu_choice = input(">>>")
        menu_choice = menu_choice.lower()
    return menu_choice


def main():
    read_file()
    menu_choice =""
    #printing the menu
    menu_choice =display_menu(menu_choice)


main()


