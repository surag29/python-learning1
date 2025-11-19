class factory:
    def __init__(self,name):
        self.name = name    # assigning to that object 
        print(f"the name of the factory is {self.name}")

bng  = factory("banglore")
chn = factory("chennai")


# intance method 
class func:
    def addition(self,a,b):
        self.a = a
        self.b = b
        print(f"the sum of the values if {a+b}")

    @classmethod
    def puc(cls):
        print("this is a  class method ")
    
    @staticmethod
    def stats():
        print("this is a static method ")

obj = func()
obj.addition(45,100)
obj.puc()

obj.stats()

