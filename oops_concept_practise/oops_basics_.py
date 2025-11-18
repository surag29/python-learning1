class addition:
    type = "animal"
   


    def __init__(self,a,b):
        print(a+b)

    def animal(self):
        print("bow bow ")

obj = addition(45,55)
print(obj.type)
obj.animal()


# here the slef addresses the location of the object and the innit method is a dunder method constructor 