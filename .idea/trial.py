

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


def read_file():
    global required_books
    global completed_books
    global index_value
    datum = []
    all_books= []
    required = "r"
    completed = "c"
    file_pointer= open(FILENAME, "r")
    for index, data in enumerate(file_pointer.readlines()):
        data = data.strip()
        datum = data.split(",")
        #index_value = str(index)
        #datum.append(index_value)
        all_books.append(datum)
    all_books.sort(key=itemgetter(1,2))
    for i in range(len(all_books)):
        index_value = str(i)
        all_books[i].append(index_value)
    for i in range(len(all_books)):
        if all_books[i][3] == "r":
            required_books.append(all_books[i])
        if all_books[i][3] == "c":
            completed_books.append(all_books[i])

    file_pointer.close()



def display_menu():
    """
    The display_menu function is used to display the menu and checks whether the entered menu choice is valid
    :return: returns the menu choice of the user
    """

    counter = True
    #print("")
    print("""Menu:
R - List required books
C - List completed books
A - Add new book
M - Mark a book as completed
Q - Quit """)
    menu_choice = input(">>>")
    menu_choice = menu_choice.lower()
    while(counter == True):


        if (menu_choice == "r" or menu_choice == "c" or menu_choice == "a" or menu_choice == "m" or menu_choice == "q"):
            return menu_choice
            counter = False
            break


        if (counter== True):
            print("Invalid menu choice")
            print("""Menu:
R - List required books
C - List completed books
A - Add new book
M - Mark a book as completed
Q - Quit """)
            menu_choice = input(">>>")
            menu_choice = menu_choice.lower()



def listing_books(list_book):
    total_pages=0
    count =0
    list_book.sort(key=itemgetter(4, 2))

    for i in range (len(list_book)):
        print(" {0}.  {1:40s} by {2:20s} {3:} pages".format(list_book[i][4],list_book[i][0],list_book[i][1], list_book[i][2]))
        total_pages = total_pages + int(list_book[i][2])
        count +=1
    if count==1 :
        print("Total pages for {} book : {}".format(count, total_pages))
    elif count>1 :
        print("Total pages for {} books : {}".format(count, total_pages))
    else:
        print("No books")


def marking_books(required_books,completed_books):

    print("Enter the number of a book to mark as completed")
    count = 0
    while(True):
        if len(required_books)==0:
            break
        try:
            marked_book_number = int(input(">>>"))
            for i in range(len(required_books)):
                if (marked_book_number == int(required_books[i][4])):
                    print("{} by {} marked as completed".format(required_books[i][0], required_books[i][1]))
                    required_books[i][3] = "c"
                    completed_books.append(required_books[i])
                    required_books.pop(i)
                    count+=1
                    break
            if count>0 :
                break
            if count == 0 :
                for i in range(len(completed_books)):
                    if (marked_book_number == int(completed_books[i][4])):
                        print("That book is already completed")
                        count+=1
                        break
                break

            if count == 0:
                print("Invalid book number")

        except ValueError:
            print("Invalid input; enter a valid number")


def adding_books(index_value,required_books):

    data =[]
    title=input("Title:")
    while not title.strip():
        print("Input cannot be blank")
        title = input("Title:")
    data.append(title)
    author = input("Author:")
    while not author.strip():
        print("Input cannot be blank")
        author = input("Author:")
    data.append(author)
    while(True):
        try:
            pages = int(input("Pages:"))
            if pages < 0 :
                print("Number must be >= 0")
                continue

            else:

                break
        except ValueError:
            print("Invalid input; enter a valid number")
    value = str(pages)
    data.append(value)
    value = int(index_value)
    value = value+ 1
    index_value = str(value)
    data.append("r")
    data.append(index_value)
    required_books.append(data)
    print("{} by {} , ({} pages) added to reading list ".format(title,author,pages))

def write_file():
    list_books=[]
    dataValue = ""
    for i in range(len(required_books)):
        list_books.append(required_books[i])
    for i in range(len(completed_books)):
        list_books.append(completed_books[i])
    list_books.sort(key=itemgetter(4, 2))

    outFile = open(FILENAME, "w")

    for i in range(len(list_books)):
        data = list_books[i][:4]

        for j in range(4) :
            #dataValue = str(data[j:j+1])
            dataValue = data[j]
            outFile.write(dataValue)
            if j<3:
                outFile.write(",")
            else:
                outFile.write("\n")
    outFile.close()



def main():
    read_file()

    #printing the menu
    print("""Reading List 1.0 - by Vihangi Vagal
{} books loaded from {}""". format(int(index_value)+1,FILENAME))
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
            adding_books(index_value,required_books)
            menu_choice = display_menu()
        elif menu_choice == "m":
            print("Required books:")
            listing_books(required_books)
            marking_books(required_books,completed_books)
            menu_choice = display_menu()

        else:
            print("invalid")
    if menu_choice == "q":
        print("{} books saved to {} \nHave a nice day :)".format(int(index_value)+1, FILENAME))

main()


