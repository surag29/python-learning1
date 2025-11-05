class dog:
    def __init__(self):
        print("the constructor of the dog class")
    a =1
class dogesh(dog):
    def __init__(self):
     super().__init__()
     print("the constructor of the dogesh class")
    b=2 
class dogeshbhai(dogesh):
 
    def __init__(self):
        super().__init__()
        print("the constructor of the dogeshbhai class")
    c= 3
 

o = dogeshbhai()
print(o.a,o.b,o.c)