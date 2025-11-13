class student:
    marks = int(input("enter the marks "))
    roll = int (input("enter the roll "))
    name =  input("enter the name ")
    def printdetails(self):
        print(self.name)
        print(self.roll)
        print(self.marks)
    def passf(self):
        if(self.marks>35):
            print(f"the {self.name},has passed with marks {self.marks}")
s = student()
s.printdetails()
s.passf()