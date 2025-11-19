class twod:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"the vectors are {self.i} and {self.j}")
    
class threed(twod):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def show(self):
            print(f"the vectors are {self.i} and {self.j} and {self.k}")

a = twod(1,2)
a.show()
b = threed(5,2,3)
b.show()