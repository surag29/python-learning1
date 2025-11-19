'''
Polymorphism
 24
 Polymorphism is a core concept in Object-Oriented Programming 
(OOP). The word means "many forms" — and in programming, it 
allows the same interface or method name to behave differently 
depending on the object or context.
 Types of Polymorphism
 Polymorphism can be achieved in python in two ways well if we 
talk about compile time languages there are 3 ways but python 
does not support Method overloading
 Method overloading means having same name methods inside a 
class but parameters will be different but in python the latest 
definition will overwrite the previous one
'''

class animal:
    def show(self):
        print("hey how are you ")

class dog(animal):
    def show(self):
        print("bow bow bow bow ")

obj = dog()
obj.show()


#this is an exmaple of method over riding

''' Duck Typin
 Python follows the philosophy:
 “If it walks like a duck and quacks like a duck, it must be a 
duck.'''

class human:
    def display(self):
        print("how are you ")

class child:
    def display(self):
        print("yay yay ya")

obj = human()
obj.display()

obj = child()
obj.display()

