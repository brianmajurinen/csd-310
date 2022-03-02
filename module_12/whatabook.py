#Brian Majurinen
#CYBR410-H331
#February 28, 2022

import sys
import mysql.connector

#database config. I've had trouble with adding users. Please add your password in the password field for this to work
config = {
    "user": "root",
    "password": "!M!ysql123",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}
#FUNCTIONS. These are the functions that will be called

#Menu function. Showing the user the main menu
def show_menu():
    print("Main Menu. Please select an option")

    print("1. View Books\n 2. View Store Locations\n 3. My Account\n 4. Exit")

    try:
        choice = int(input('Please select an option '))

        return choice
    except ValueError:
        print("\n  Invalid option. Ending program.")

        sys.exit(0)

#Show books function. Borrowed this from the solution. This function performs the join to show the listing of books
def show_books(_cursor):
    # inner join query 
    _cursor.execute("SELECT book_id, book_name, author, details from book")

    # get the results from the cursor object 
    books = _cursor.fetchall()

    print(" Books\n")
    
    # iterate over the player data set and display the results 
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2]))

#Show locations function. There is only one location
def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")

    locations = _cursor.fetchall()

    print("\n Store locations")
    #This for loop will print every location. There is only one iteration of this loop.
    for location in locations:
        print("  Locale: {}\n".format(location[1]))

#Function to validate the user's ID. There are only 3 valid users
def validate_user():

    try:
        user_id = int(input('Please enter ID number: '))

        if user_id < 0 or user_id > 3:
            print("\n Invalid.\n")
            sys.exit(0)

        return user_id
    except ValueError:
        print("\n Invalid.\n")

        sys.exit(0)

#This function shows options if My Account is chosen
def show_account_menu():

    try:
        print("\n      -- Customer Menu --")
        print("        1. Wishlist\n        2. Add Book\n        3. Main Menu")
        account_option = int(input('        <Example enter: 1 for wishlist>: '))

        return account_option
    except ValueError:
        print("\n  Invalid number, program terminated...\n")

        sys.exit(0)

def show_wishlist(_cursor, _user_id):
    """ query the database for a list of books added to the users wishlist """

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = _cursor.fetchall()

    print("\n Wishlist Items")

    for book in wishlist:
        print("        Book Name: {}\n        Author: {}\n".format(book[4], book[5]))

def show_books_to_add(_cursor, _user_id):
    """ query the database for a list of books not in the users wishlist """

    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n        -- DISPLAYING AVAILABLE BOOKS --")

    for book in books_to_add:
        print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

#This is the main program. Pieces are from earlier assignments. I have a heck of a hard time with this.
#My python skills are not up to snuff so I've used the solution a lot. Sorry.
try:
    #connecting to the database
    db = mysql.connector.connect(**config)

    cursor = db.cursor()
    
    #calling the show_menu function
    user_selection = show_menu() 

    # while the user's selection is not 4
    while user_selection != 4:

        # if the user selects option 1, call the show_books method and display the books
        if user_selection == 1:
            show_books(cursor)

        # if the user selects option 2, call the show_locations method and display the configured locations
        if user_selection == 2:
            show_locations(cursor)

        # if the user selects option 3, call the validate_user method to validate the entered user_id 
        # call the show_account_menu() to show the account settings menu
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            # while account option does not equal 3
            while account_option != 3:

                # if the use selects option 1, call the show_wishlist() method to show the current users 
                # configured wishlist items 
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                # if the user selects option 2, call the show_books_to_add function to show the user 
                # the books not currently configured in the users wishlist
                if account_option == 2:

                    # show the books not currently configured in the users wishlist
                    show_books_to_add(cursor, my_user_id)

                    # get the entered book_id 
                    book_id = int(input("\n        Enter the id of the book you want to add: "))
                    
                    # add the selected book the users wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    db.commit() # commit the changes to the database 

                    print("\n        Book id: {} was added to your wishlist!".format(book_id))

                # if the selected option is less than 0 or greater than 3, display an invalid user selection 
                if account_option < 0 or account_option > 3:
                    print("\n      Invalid option, please retry...")

                # show the account menu 
                account_option = show_account_menu()
        
        # if the user selection is less than 0 or greater than 4, display an invalid user selection
        if user_selection < 0 or user_selection > 4:
            print("\n      Invalid option, please retry...")
            
        # show the main menu
        user_selection = show_menu()

    print("\n\n  Program terminated...")

finally:
    """ close the connection to MySQL """

    db.close()
