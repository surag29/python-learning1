# this is a multiple inheritance example

class animal:
    def typeof(self):
        print("the type of animal is ")

class dog():
    def dogesh(self):
        print("this is a dog ")

class puppy(animal,dog):
    def puppies(self):
        print("this is a puppy")


dg = puppy()
dg.dogesh()
dg.typeof()
dg.puppies()


# this is a multilevel inheritance

class animal:
    def typeof(self):
        print("the type of animal is ")

class dog(animal):
    def dogesh(self):
        print("this is a dog ")

class puppy(dog):
    def puppies(self):
        print("this is a puppy")


dg = puppy()
dg.dogesh()
dg.typeof()
dg.puppies()


class show:
    def __init__(self,name):
        self.name =  name

class display(show):
     def __init__(self, name,age):
         super().__init__(name)
         self.age = age
         print(f"the name is  {self.name}, the age is {self.age}")

obj1 = display("surag",22)