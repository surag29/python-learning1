from abc import ABC , abstractmethod

class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def sqaure(self):
        pass

class circle(abstract):
    def __init__(self,radius):
        self.radius = radius
    def perimeter(self):
        print("this is implemented")
    def sqaure(self):
        print("this is also implemented")

class cube(abstract):
    def __init__(self,side):
        self.side = side
    def perimeter(self):
        print("this is implemented")
    def sqaure(self):
        print("this is also implemented")

#/obj = cube(12)
ob1 = circle(15)






