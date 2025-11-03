'''2. Write a class “Calculator” capable of finding square, cube and square root of a 
number. '''

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        return self.n * self.n
    
    def cube(self):
        return self.n*self.n*self.n
    
    def squareroot(self):
        return self.n**1/2


c = Calculator(4)
print(f"The square of the number is: {c.square()}")
print(f"The square of the number is: {c.cube()}")
print(f"The square of the number is: {c.squareroot()}")

