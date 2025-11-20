import json
from pathlib import Path

class Library:
    database ="data.json"
    memberDb = "member.json"
    data=[]
    members =[]
    try:
        if Path(database).exists():
            with open(database) as fs:
                data= json.loads(fs.read())
        else:
            print("no such file exist")

        if Path(memberDb).exists():
          with open(memberDb) as fs:
             members = json.loads(fs.read())
        else:
           print("no such file exist")
    except Exception as err:
        print(f"an exception occur as {err}")

        

    @classmethod
    def __update(cls):
        with open(Library.database, "w") as fs:
            fs.write(json.dumps(Library.data))

    @classmethod
    def __updateMembers(cls):
        with open(Library.memberDb, "w") as fs:
            fs.write(json.dumps(Library.members))
    def member(self):
        info={
            "name": input("enter your name:- "),
            "email": input("enter your email:- "),
            "issuedBooks": []
        }
        Library.members.append(info)
        Library.__updateMembers()


    def add_book(self):
        book_info ={
            "Title": input("enter the name of book:- "),
            "Author": input("enter the name of author:- "),
            "Category": input("category:- "),
            "Publication year": int(input("Year of publication:- ")),
            "ISBN": int(input("ISBN:- ")),
            "Total copies": int(input("Total number of copies:- ")),
            "Available copies": int(input("Available copies:- ")),
            "Description": input("Description:- ")
        }
        Library.data.append(book_info)
        Library.__update()
    
    def showBookDDetails(self):
        Title= input("Enter the title of book you want to search:- ")
        ISBN = int(input("Enter the isbn:- "))

        Book = [i for i in Library.data if i["Title"]== Title and i["ISBN"]== ISBN]

        for i in Book[0]:
            print(f"{i}: {Book[0][i]}")

    def issueBook(self):
        name = input("enter your name:- ")
        email = input("enter your email:- ")
        bookTitle =input("enter a book name you want:- ")
        ISBN = int(input("Enter the isbn:- "))

        memberData =[i for i in Library.members if i["name"]== name and i["email"]== email]
        bookData = [i for i in Library.data if i["Title"]== bookTitle and i["ISBN"]== ISBN]

        if memberData == False and bookData == False:
            print("No such book or member exist")

        else:
            if bookData[0]["Available copies"]<=0:
                print("the book is not assignable")
            elif bookData[0]["Available copies"] > bookData[0]["Total copies"]:
                print(" AAvailable copies  must be less then or equal to total copies")


            memberData[0]["issuedBooks"].append(bookData[0])
            bookData[0]["Available copies"]-= 1
            Library.__updateMembers()
            Library.__update()
    def returnBook(self):
        name = input("enter your name:- ")
        email = input("enter your email:- ")
        bookTitle =input("enter a book name you want to return:- ")
        ISBN = int(input("Enter the isbn:- "))

        memberData =[i for i in Library.members if i["name"]== name and i["email"]== email]
        bookData = [i for i in Library.data if i["Title"]== bookTitle and i["ISBN"]== ISBN]

        if memberData == False and bookData == False:
            print("No such book or member exist")

        else:
            if bookData[0]["Available copies"]<=0:
                print("the book is not assignable")
            elif bookData[0]["Available copies"] > bookData[0]["Total copies"]:
                print(" AAvailable copies  must be less then or equal to total copies")


            memberData[0]["issuedBooks"].remove(bookData[0])
            bookData[0]["Available copies"]+= 1
            Library.__updateMembers()
            Library.__update()



print("press 1 to register")
print("press 2 to add a book")
print("press 3 to search book")
print("press 4 to issue a book")
print("press 5 to return a book")

check =  int(input("Enter what you want to do:- "))


library = Library()
if check ==1:
    library.member()

if check == 2:
    library.add_book()

if check ==3:
    library.showBookDDetails()

if check == 4:
    library.issueBook()

if check == 5:
    library.returnBook()


