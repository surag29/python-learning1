'''   Encapsulation
 25
 Encapsulation means putting data (variables) and code (functions) 
together in one place — inside a class
 It also means hiding the internal details of how things work, and 
only showing what is needed
 It keeps data safe from being changed by mistake
 It makes your code clean and easy to use
 It gives control over what others can access or change'''

class human:
    __a = "surag"
    def show(self):
        print(f"the name is is  {human.__a}")

class animal(human):
    def show2(self):
        print(f"the name is {super().__a}")

obj = animal()
obj.show2()

obj1 = human()
obj1.show()



'''  Private Attributes and Method
 A private variable or method means
 It cannot be accessed from outside the class — only from 
inside the class where it is defined
 In Python, we use two underscores (__) before the name to 
make it private.'''