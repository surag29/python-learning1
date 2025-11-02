class employee:
    language =  "python"  #this are class attributes
    salary = 120000



    
    def __init__(self,name,language,salary,exp):
        self.name = name
        self.language = language
        self.salary = salary
        self.exp = exp

        print("this is a dunder method ,constructor which gets called automatically when an object is created")


    def getinfo(self):
        print(f"the language is {self.language} and the salary is {self.salary}" )


surag = employee("surag","c++",130000,3)

surag.getinfo()

# employee.getinfo(surag)

# surag.name = "suru" # object attributes

print(surag.name,surag.language,surag.salary,surag.exp)
    
    