

"""
Name : Vihangi Vagal
Date : 27th December 2016
Program details : This program reads a file and loads the books from that file. It allows the user to mark the books
completed.A list of required books and completed books are also listed. The program also allows the user to add books.
At the end the data is rewritten in the file.

GitHub link :https://github.com/vihangi/Programming1_assignment1.git
"""

from operator import itemgetter
#defining the variables
FILENAME = "books.csv"
required_books=[]
add_books=[]
completed_books =[]
marked_books=[]


def read_file():
    """
    This function loads the file and reads all the data. It stores the data onto a list. The list is then sorted and
    appended with index numbers according to the authors name . It also seperates the data into required_books and
    completed_books list based on whether its third index is "r" or "c" respectively.
    :return: null
    """
    #defining these variables as global so that they can be called in any function
    global required_books
    global completed_books
    global index_value
    datum = []
    all_books= []
    required = "r"
    completed = "c"
    file_pointer= open(FILENAME, "r")
    #reading the file
    for index, data in enumerate(file_pointer.readlines()):
        data = data.strip()
        datum = data.split(",")
        all_books.append(datum)
    all_books.sort(key=itemgetter(1,2))
    #distrubuting the data into required_books and completed_books
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
    print("""Menu:
R - List required books
C - List completed books
A - Add new book
M - Mark a book as completed
Q - Quit """)
    menu_choice = input(">>>")
    menu_choice = menu_choice.lower()
    #this prints the menu until the user enter a valid input
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



def listing_books(list_book,menu_choice):
    """
    This function is used to sort and list all the books in the list . It aligns all the data in the list in a table format.
    :param list_book: This is used to store the list which needs to be displayed
    :param menu_choice: stores menu choice
    :return: null
    """
    total_pages=0
    count =0
    #sorting the list
    list_book.sort(key=itemgetter(4, 2))
    #printing the list
    if (len(list_book)>0):
        for i in range (len(list_book)):
            print(" {0}.  {1:40s} by {2:20s} {3:} pages".format(list_book[i][4],list_book[i][0],list_book[i][1], list_book[i][2]))
            total_pages = total_pages + int(list_book[i][2])
            count +=1
        #printing the count of total pages
        if count==1 :
            print("Total pages for {} book : {}".format(count, total_pages))
        if count>1 :
            print("Total pages for {} books : {}".format(count, total_pages))

    else:
        if menu_choice == "m":
            print("No required books")
            pass
        else:
            print("No books")


def marking_books(required_books,completed_books):
    """
     This function asks the user to enter a valid book number from the required list which it can mark as complete. It
    checks whether the input is correct and it also appends the complete_books list and removes that book from the
    required_books list.
    :param required_books: This stores the required list of books
    :param completed_books: This stores the completed list of books

    :return:
    """
    if (len(required_books)>0):
        print("Required books:")
        print("Enter the number of a book to mark as completed")
        count = 0
        while(True):
            if len(required_books)==0:
                break
            try:
                marked_book_number = int(input(">>>"))
                for i in range(len(required_books)):
                    #checks whether the input is in the list of required_books
                    if (marked_book_number == int(required_books[i][4])):
                        print("{} by {} marked as completed".format(required_books[i][0], required_books[i][1]))
                        required_books[i][3] = "c"
                        completed_books.append(required_books[i])
                        required_books.pop(i)
                        count+=1
                        break

                if count > 0 :
                    break
                #checks whether the input is in the list of completed_books
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

    else:
        pass


def adding_books(index_value,required_books):
    """
    This function is used to add a new book . The user is asked for a valid title, author and pages.
    It then adds the book to the require list of books.
    :param index_value: This stores the last number of the book which was added
    :param required_books: this stores the list of books required
    :return: null
    """

    data =[]
    #checks whether entered data is blank or not
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
    #checks whether the pages entered is valid or not
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
    #stores the new book in required_books
    required_books.append(data)
    print("{} by {} , ({} pages) added to reading list ".format(title,author,pages))

def write_file():
    """
    This functions creates a single list where it stores all the books . It then rewrites all the data onto the file
    :return: null
    """
    list_books=[]
    dataValue = ""
    #stores all the books in one single list
    for i in range(len(required_books)):
        list_books.append(required_books[i])
    for i in range(len(completed_books)):
        list_books.append(completed_books[i])
    list_books.sort(key=itemgetter(4, 2))
    #opens the file to rewrite
    outFile = open(FILENAME, "w")

    for i in range(len(list_books)):
        #slicing the data to remove the index number
        data = list_books[i][:4]
        #writing in the file
        for j in range(4) :
            dataValue = data[j]
            outFile.write(dataValue)
            if j<3:
                outFile.write(",")
            else:
                outFile.write("\n")
    outFile.close()
    print("{} books saved to {} \nHave a nice day :)".format(len(list_books), FILENAME))



def main():
    """
    This function is the main function where all the other functions are called.
    :return: null
    """
    read_file()

    #printing the menu
    print("""Reading List 1.0 - by Vihangi Vagal
{} books loaded from {}""". format(int(index_value)+1,FILENAME))
    menu_choice =display_menu()
    while(menu_choice != "q"):
        #list of required books
        if menu_choice == "r":
            print("Required books:")
            listing_books(required_books,menu_choice)
            menu_choice = display_menu()

        #list of completed books
        elif menu_choice == "c":
            print("Completed books:")
            listing_books(completed_books,menu_choice)
            menu_choice = display_menu()

        #to add a book
        elif menu_choice == "a":
            adding_books(index_value,required_books)
            menu_choice = display_menu()

        #to mark a book as complete
        elif menu_choice == "m":

            listing_books(required_books,menu_choice)

            marking_books(required_books,completed_books)
            menu_choice = display_menu()
        else:
            print("invalid")
    #when the user decides to quit
    if menu_choice == "q":
        write_file()


main()


