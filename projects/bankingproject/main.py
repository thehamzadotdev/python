

import json
from pathlib import Path
class Bank:

    database = "./data.json"
    data =[]
    try:
        if Path(database).exists:
            with open(database) as fs:
                data = json.load(fs.read())
        else:
            print("no such file exist")
    except Exception as err:
        print(f"an exception occured as {err}")
    @staticmethod
    def update():
        with open(Bank.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    def createAccount(self):
        info ={
            "name": input("enter your name:- "),
            "age": int(input("enter your age:- ")),
            "email": input("enter your email please:- "),
            "pin": int(input("enter your pin:- ")),
            "accountNumber":"1234",
            "balance": 0
        }

        if info["age"] < 18 or len(str(info["pin"])) != 4:
            print("you are not eligiable to open an account")
        else:
            print("your account has been created sucessfully")
            for i in info:
                print(f"[i] : {info[i]}")
            Bank.data.append(info)
            Bank.update()


User = Bank()
print("press 1 for creating an account:- ")

check = int(input("what do you want to do? "))

if check ==1:
    User.createAccount()
