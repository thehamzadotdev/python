

import json
from pathlib import Path
import random
import string
class Bank:

    database = "data.json"
    data =[]
    try:
        if Path(database).exists:
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exist")
    except Exception as err:
        print(f"an exception occured as {err}")
    @classmethod
    def __update(cls):
        with open(Bank.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __generateRandom(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num= random.choices(string.digits, k=3)
        spclchr = random.choices("!@#$%^&*()", k=3)
        id = alpha+num+spclchr
        random.shuffle(id)
        return "".join(id) 


    def createAccount(self):
        info ={
            "name": input("enter your name:- "),
            "age": int(input("enter your age:- ")),
            "email": input("enter your email please:- "),
            "pin": int(input("enter your pin:- ")),
            "accountNumber": Bank.__generateRandom(),
            "balance": 0
        }

        if info["age"] < 18 or len(str(info["pin"])) != 4:
            print("you are not eligible to open an account")
        else:
            print("your account has been created successfully")
            for i in info:
                print(f"[i] : {info[i]}")
            Bank.data.append(info)
            Bank.__update()
    def depositMoney(self):
        accNumber = str(input("enter your account number:- "))
        pin = int(input("enter your pin"))
        userdata = [i for i in Bank.data if i["accountNumber"]== accNumber and i["pin"] == pin]

        if userdata == False:
            print("invalid user data as data is empty")

        else:
            amount = int(input("please enter the amount you want to deposit:- "))
            if amount > 10000 and amount < 0:
                print("enter the correct amount")
            else:
                print(userdata)
                userdata[0]["balance"] += amount
                Bank.__update()
                print("amount deposited successfully")

    def withdrawMoney(self):
            accountNumber = str(input("please tell your account number:- "))
            pin= int(input("please enter your pin:- "))

            userdata = [i for i in Bank.data if i["accountNumber"] == accountNumber and i["pin"] == pin]

            if userdata == False:
                print("user data should not be empty")

            else:
                amount = int(input("enter the amount you want to withdraw"))
                if amount> userdata[0]["balance"] and amount< 0:
                    print("enter a valid amount")
                else:
                    userdata[0]["balance"] -= amount
                    Bank.__update()
                    print("amount withdrawn successfully")
    def showDDetails(self):
        accountNumber = str(input("please tell your account number:- "))
        pin= int(input("please enter your pin:- "))
        userdata = [i for i in Bank.data if i["accountNumber"] == accountNumber and i["pin"] == pin]

        for i in userdata[0]:
            print(f"{i}: {userdata[0][i]}")

    def updateDetails(self):
         accountNumber = str(input("please tell your account number:- "))
         pin= int(input("please enter your pin:- "))

         userdata = [i for i in Bank.data if i["accountNumber"] == accountNumber and i["pin"] == pin]

         if userdata == False:
                print("user data not found")
         else:
             print("you cannot update age, account number and balance")

             newData ={
                 "name": input("enter the name to update:- "),
                 "email": input("enter the email to update:- "),
                 "pin": input("enter the pin to update:- ")
             }

             if newData["name"] =="":
                 newData["name"] == userdata[0]["name"]
             if newData["email"] == "":
                 newData["email"] == userdata[0]["email"]
             if newData["pin"] == "":
                 newData["pin"] == userdata[0]["pin"]

             newData["age"] = userdata[0]["age"]
             newData["balance"] = userdata[0]["balance"]
             newData["accountNumber"] = userdata[0]["accountNumber"]

             if  type(newData["pin"]) == str:
                 newData["pin"] = int(newData["pin"])
             
             for i in newData:
                  if newData[i] == userdata[0][i]:
                      continue
                  else:
                      userdata[0][i] = newData[i]

             Bank.__update()
             print("your details are updated successfully")

    def deleteDetails(self):
         accountNumber = str(input("please tell your account number:- "))
         pin= int(input("please enter your pin:- "))

         userdata = [i for i in Bank.data if i["accountNumber"] == accountNumber and i["pin"] == pin]

         if userdata == False:
                print("user data not found")

         else:
             
             check = input("press y to delete account or N to by pass ")

             if check == "n" or check == "N":
                 pass
             else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                Bank.__update()
                print("Account has been deleted") 
                

User = Bank()
print("press 1 for creating an account:- ")
print("press 2 for deposit money in account:- ")
print("press 3 to withdraw money from account:- ")
print("press 4 for details:- ")
print("press 5 to update the details")
print("press 6 to delete the details")

check = int(input("what do you want to do? "))

if check ==1:
    User.createAccount()

if check == 2:
    User.depositMoney()
if check == 3:
    User.withdrawMoney()

if check == 4:
    User.showDDetails()

if check ==5:
    User.updateDetails()

if check == 6:
    User.deleteDetails()


