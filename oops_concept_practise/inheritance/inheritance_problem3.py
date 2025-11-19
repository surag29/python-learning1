class employee:
    salary = 245667
    increment = 20
    @property
    def salaryafterinc(self):
        return (self.salary + (self.salary*self.increment/100))
    
    @salaryafterinc.setter
    def salarafterinc(self,salary):
        self.increment = ((salary/self.salary)-1)*100



e = employee()

print(e.salaryafterinc)
# e.salarafterinc = 290000
# print(e.increment)

