class animal:
    def __init__(self,name,age):
        self.name =  name
        self.age =  age
    
    def __str__(self):
        return (f"the name is { self.name} ")
    
    def __add__(self,other):
        sum = 0
        for i in other:
            sum += i.age
        return (f"the sum of age  is {self.age + sum} ")
obj = animal("lion",22)
obj1 = animal("tiger",23)
obj2 = animal("tiger",25)
print(obj+(obj1,obj2))
         


          