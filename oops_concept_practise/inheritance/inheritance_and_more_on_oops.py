class company:
    companyname = "microsoft"

    def comshow(self):
        print(f"The company name is {self.companyname}")

class manager(company):        # INHERITANCE
    managername = "suru"

    def manshow(self):
        return (f" {self.managername} {self.companyname}")

class employee(manager):         # MULITlevel INHERITANCE
    employee_name = "suruuu"
    def getinfo(self):
        print(f"the employee name is {self.employee_name} and his manager and company is  {self.manshow()}")

o = employee()
o.getinfo()


# multiple inheritance
class dog:
    dog_name = "husky"
    def dogshow(self):
     print(f"the dog name is {self.dog_name}")
class puppy:
    puppy_name = "mini_husky"
    def puupyshow(self):
     print(f"the dog name is {self.puppy_name}")
class suppuppy(dog,puppy):
    super_puppy_name = "super husky"
    def getinfo(self):
     print(f"the name of the dog and mini puppy and super puppy is {self.dog_name},{self.puppy_name},{self.super_puppy_name}")
o = suppuppy()
o.dogshow()
o.puupyshow()
o.getinfo()



