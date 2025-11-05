class funct:
    a = 1
    def show(self):
     print(f"the value of a is {self.a}")
b = funct()
b.a = 45 #instance attribute will be printed
b.show()

'''to access the class values not to be overwritten  by the instance attribute we use @classmethod'''



class functt:
    a = 1
    @classmethod
    def show(cls):
     print(f"the value of a is {cls.a}")
b = functt()
b.a = 45 #instance attribute will be printed
b.show()

