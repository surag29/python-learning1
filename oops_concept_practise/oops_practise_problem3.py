'''3. Create a class with a class attribute a; create an object from it and set ‘a’ 
directly using ‘object.a = 0’. Does this change the class attribute?'''

class demo:
    a = 4 # class attribute

c = demo()
print(c.a)  #class attribute is printed
c.a = 0     #instance attribute is set
print(c.a)  #instance attribute is printed
print(demo.a) #class attribute is printed and it is not changed