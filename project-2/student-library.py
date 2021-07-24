import os
os.system("cls")

class Library:

    # Constructor
    def __init__(self,listOfBooks) :
        self.books = listOfBooks

    def displayAvailableBooks(self) :
        print("Books present in this library are : \n")
        for index,book in enumerate(self.books) :
            print(f"{index+1}) {book}")
    
    def borrowBook(self,bookName) :
        if bookName in self.books :
            print("You have been issued {}, Please return it within 30 days".format(bookName))
            self.books.remove(bookName)
            return True
        else :
            print("Sorry, This book either not available or has already been issued. Please wait until the book is available")
            return False

    def returnBook(self,bookName) :
        self.books.append(bookName)
        print("Thanks for adding/returning this book, Hope you enjoyed reading it")
    
    

class Student :

    def requestBook(self) :
        self.book = input("Enter the name of the book you want to borrow : ")
        return self.book

    def returnBook(self) :
        self.book = input("Enter the name of the book you want to add/return : ")
        return self.book


if __name__ == "__main__" :
    
    l = Library(["Algorithims","Django","ReactJs","CSS","HTML"])
    student = Student()

    while(True) :
        welcomeMsg = '''\n===== Welcome to Centeral Library =====
        Please choose an option :
        1) listing all the books
        2) Request a book
        3) Add/Return a book
        4) Exit library\n
        '''

        print(welcomeMsg)

        a = int(input("Enter a choice : "))

        if a == 1 :
            l.displayAvailableBooks()

        elif a == 2 :
            l.borrowBook(student.requestBook())

        elif a == 3 :
            l.returnBook(student.returnBook())

        elif a == 4 :
            print("Thanks for using Central library")
            exit()

        else :
            print("Invalid Choice")

        