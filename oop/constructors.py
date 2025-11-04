class bank:
    def __init__(self,name,email,phone,accountnumber):
        self.name= name
        self.email= email
        self.phone= phone
        self.accountnumber= accountnumber

    def show(self):
        print(f"your account details are name:{self.name}, email:{self.email}, phone: {self.phone}, accountnumber:{self.accountnumber}")


acc1= bank("hamza", "hamza@gmail.com", "03025280190", "0713548281")

acc1.show()


# SElF constructor to access the location of variable