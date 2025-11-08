class animal:
    pass
class pets(animal):
    pass
class dog(pets):
    @staticmethod
    def bark():
        print("now now")
d = dog()
d.bark()