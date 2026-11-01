#classes
#customer  - names, email, kra, dob, gender
#BankAccount -  Customer, acc_no, acc_type, balance


class Customer:
    def __init__(self, names, email, kra, dob, gender):
        self.names = names
        self.email = email
        self.kra = kra
        self.dob = dob
        self.gender = gender
    def print_details(self):
        print(f"Name: {self.names} and KRA PIN:{self.kra}")
        # return f"Name:{self.names} and KRA PIN : {self.kra}"

class Account:
    def __init__(self, owner:Customer, acc_no:str, acc_type:str, balance:float):
        self.owner = owner
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.balance = balance

    def print_details(self):
        print(self.owner.names)
        print(self.acc_no)
        print(self.balance)
        print("***************")
    def deposit(self, amount:float):
        self.balance += abs(amount)

    def withdraw(self, amount:float):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= abs(amount)
    def __abs__(self):
        return f"Account No {self.acc_no} for {self.owner.names}"

owner1 = Customer("Jim Jong", "jj@test.com", "KRA001", "31-8-1980", "Male")
owner2 = Customer("Vera Michael", "vm@test.com", "KRA002", "25-1-1980", "Female")

acc1 = Account(owner1, "98765", "current", 80_000)
acc2 = Account(owner1, "98766", "current", 1_000_000.50)
acc3 = Account(owner1, "98767", "current", 71_000.00)


# print(owner1.dob)
# print(owner1.show_detail())

acc1.print_details()
acc1.deposit(-9000)
acc1.print_details()
acc1.print_details()


print(acc1.owner)





