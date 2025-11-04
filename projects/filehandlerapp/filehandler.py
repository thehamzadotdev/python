
from pathlib import Path
import os

def readfileandfolder():
    path = Path("")
    items= list(path.rglob("*"))
    for i, items in enumerate(items):
        print(f"{i+1}  : {items} ")

def createfile():
    try:
          readfileandfolder()
          name=input("enter the name of file:- ")
          p=Path(name)
          if not p.exists():
               with open(p,"w") as fs:
                    data= input("what ddo you want to write in this file:- ")
                    fs.write(data)
                    print("file created successfully")
          else:
               print("file already exist")
    except Exception as err:
         print(f"An error occurred as {err}")


def readfile():
     try:
          readfileandfolder()
          name= input("enter the name of file to read:- ")
          p= Path(name)
          if p.exists() and p.is_file:
               with open(p,"r") as fs:
                    data= fs.read()
                    print(data)
          else:
               print("the file does not exist")


     except Exception as err:
          print(f"An error occurred as {err}")


def updatefile():
     try:
          readfileandfolder()
          name= input("enter the name of file you want to update:- ")
          p= Path(name)
          if p.exists() and p.is_file:
                 print("press 1 for changing the name of your file :- ")
                 print("press 2 for overwriting the data of your file:- ")
                 print("press 3 for appending some content in your file:-  ")

                 res= int(input("what operation do you want to perform? "))

                 if res == 1:
                      name2= input("enter the updated name of file:- ")
                      p2= Path(name2)
                      p.rename(p2)
                 if res == 2:
                      with open(p, "w") as fs:
                           data= input("what do you want to overwrite in a file? ")
                           fs.write(data)
                 if res == 3:
                      with open(p, "a") as fs:
                           data= input("what do you want to append? ")
                           fs.write(" "+data)

     
     except Exception as err:
          print(f"An error occurred as {err}")

def deletefile():
     try:
          readfileandfolder()
          name = input("enter the name of file you wanna delete:- ")
          p= Path(name)
          if p.exists() and p.is_file:
               os.remove(name)
               print("file removed successfully")
          else:
               print("unable to remove a file")

     except Exception as err:
          print(f"An error occurred as {err}")
     


print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deletion a file")

check = int(input("enter a number to perform operation:- "))


if check ==1:
     createfile()
if check ==2:
     readfile()
if check == 3:
     updatefile()
if check == 4:
     deletefile()