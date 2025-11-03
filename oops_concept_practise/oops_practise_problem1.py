
''''1. Create a class “Programmer” for storing information of few programmers 
working at Microsoft. '''

class programmer:
    company =  "microsoft"

    def __init__(self,name,salary,pin):
        self.name = name
        self.salary =  salary
        self.pin =  pin
p =  programmer("surag",90000,585103)
print(p.name,p.salary,p.company,p.pin)
r =  programmer("suru",90000,585103)
print(r.name,r.salary,r.company,r.pin)
    