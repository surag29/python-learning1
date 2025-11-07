class Car:
    def __init__(self, brand, model):
        # complete this
        self.brand = brand
        self.model = model

c1 = Car("tesla","model 3")
c2 = Car("bmw", "x5")

print(c1.brand,c1.model)
print(c2.brand,c2.model)
# Create two car objects:
# 1. Tesla Model 3
# 2. BMW X5

# Print their brand and model separately

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"name {self.name},marks:{self.marks}")

s1 = Student("surag",100)
s2 = Student("suru",99)
s1.display()
s2.display()
    # create a method 'display' that prints "Name: ___, Marks: ___"

# Create two students and call display()

class Employee:
    company = "Google"

    def __init__(self, name):
        self.name = name
    @classmethod
    def show_company(cls):
     print(f"the company is {cls.company}")
e1 = Employee("surag")
e2 = Employee("suru")
e1.show_company()
e2.show_company()

    # add a classmethod called 'show_company' that prints company name

# Create two employees and call the method
class Math:
    @staticmethod
    def add(a, b):
        return a+b
    
print(Math.add(133,144))

# Call without creating object

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    @property
    def name(self):
        return (f"the name is {self.fname}{self.lname}")
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

p = Person("surag","devadiga")
p.name = "surag Devadiga"
print(p.name)



    # make a property 'fullname' that joins fname and lname
    # also make a setter to split full name into fname, lname

# Create object, print fullname, then set fullname to "Ravi Kumar" and print again

class BankAccount:
    # Class variable (common to all accounts)
    bank_name = "SBI"

    def __init__(self, holder, balance):
        # Instance variables (unique to each account)
        self.holder = holder
        self.balance = balance

    @classmethod
    def change_bank(cls, new_bank):
        # cls refers to the class itself
        cls.bank_name = new_bank
        print(f"Bank name changed to {cls.bank_name}")

    @staticmethod
    def interest(principal, rate, time):
        # No need for self or cls, just simple calculation
        # Simple Interest = (P × R × T) / 100
        return (principal * rate * time) / 100

    @property
    def info(self):
        # Acts like a read-only attribute
        return f"Holder: {self.holder}, Balance: ₹{self.balance}"

# --- Testing all methods ---

# Create account objects
a1 = BankAccount("Surag", 10000)
a2 = BankAccount("Dev", 5000)

# Property: Access account info
print(a1.info)   # Holder: Surag, Balance: ₹10000
print(a2.info)   # Holder: Dev, Balance: ₹5000

# Static method: calculate interest
print("Interest:", BankAccount.interest(10000, 5, 2))  # 1000.0

# Class method: change bank name
BankAccount.change_bank("HDFC")

# Confirm change
print(f"a1 bank: {a1.bank_name}")
print(f"a2 bank: {a2.bank_name}")
