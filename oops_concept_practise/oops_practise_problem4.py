'''4. Add a static method in problem 2, to greet the user with hello. '''

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        return self.n * self.n
    
    def cube(self):
        return self.n*self.n*self.n
    
    def squareroot(self):
        return self.n**1/2
    
    @staticmethod
    def greet():
        print("hello hi there")


c = Calculator(4)
c.greet()
print(f"The square of the number is: {c.square()}")
print(f"The square of the number is: {c.cube()}")
print(f"The square of the number is: {c.squareroot()}")