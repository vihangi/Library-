

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
        index_value = str(index)
        #print(index_value)
        #print(index, datum)
        datum.append(index_value)
        if datum[3] == "r":
            required_books.append(datum)

        if datum[3] == "c":
            completed_books.append(datum)
    file_pointer.close()

def display_menu():
    """
    The display_menu function is used to display the menu and checks whether the entered menu choice is valid
    :return: returns the menu choice of the user
    """
    counter = True
    print("")
    print(""" Menu:
                      R - List required books
                      C - List completed books
                      A - Add new book
                      M - Mark a book as completed
                      Q - Quit

                      """)
    menu_choice = input(">>>")
    menu_choice = menu_choice.lower()
    while(counter == True):


        if (menu_choice == "r" or menu_choice == "c" or menu_choice == "a" or menu_choice == "m" or menu_choice == "q"):
            return menu_choice
            counter = False
            break


        if (counter== True):
            print("Invalid menu choice")
            print(""" Menu:
                                  R - List required books
                                  C - List completed books
                                  A - Add new book
                                  M - Mark a book as completed
                                  Q - Quit

                                  """)
            menu_choice = input(">>>")
            menu_choice = menu_choice.lower()



def listing_books(list_book):
    total_pages=0
    count =0
    list_book.sort(key=itemgetter(4, 2))
    for i in range (len(list_book)):
        print("{0}.{2:10s} {1:10s} {2:10s}by {3:20s} {4:>20s} pages".format(list_book[i][4],list_book[i][0],"",list_book[i][1], list_book[i][2]))
        total_pages = total_pages + int(list_book[i][2])
        count +=1
    if count==1 :
        print("{:<10s}Total pages for {} book : {}".format("", count, total_pages))
    elif count>1 :
        print("{:<10s}Total pages for {} books : {}".format("", count, total_pages))
    else:
        print("No books")

def marking_books(required_books,completed_books):

    print("Enter the number of a book to mark as completed")
    count = 0
    try:
        marked_book_number = int(input(">>>"))
        for i in range(len(required_books)):
            if (marked_book_number == int(required_books[i][4])):
                completed_books.append(required_books[i])
                required_books.pop(i)
                print("{} by {} marked as completed".format(completed_books[i][0],completed_books[i][1]))
                count+=1
                break

        if count == 0 :
            for i in range(len(completed_books)):
                if (marked_book_number == int(completed_books[i][4])):
                    print("Book already completed")
                    count+=1

        if count == 0:
            print("Invalid book number")
            marking_books(required_books,completed_books)


    except ValueError:
        if marked_book_number== 0:
            pass
        else:
            print("Invalid input; enter a valid number")
            marking_books(required_books,completed_books)

def main():
    read_file()

    #printing the menu
    print("""Reading List 1.0 - by Vihangi Vagal
    4 books loaded from {}""". format(FILENAME))
    menu_choice =display_menu()
    while(menu_choice != "q"):
        if menu_choice == "r":
            print("Required books:")
            listing_books(required_books)
            menu_choice = display_menu()
        elif menu_choice == "c":
            print("Completed books:")
            listing_books(completed_books)
            menu_choice = display_menu()
        elif menu_choice == "a":
            print("Add books:")
            menu_choice = display_menu()
        elif menu_choice == "m":
            print("Required books:")
            listing_books(required_books)
            marking_books(required_books,completed_books)
            menu_choice = display_menu()
        elif menu_choice == "q":
            print("quit")
        else:
            print("invalid")


main()


