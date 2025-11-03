'''5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under Indian Railways. '''

from random import randint

class train:
    def __init__(self,trainNO):
        self.trainNO = trainNO

        

    def book(self,FRO,TO):
        print(f"the trainno :{self.trainNO}  booked from : {FRO} to : {TO}" )
    
    def getstatus(self):
        print(f"the train {self.trainNO} is running successfully on time")
    
    def getfair(self,FRO,TO):
        print(f"the ticket fair in trainno :{self.trainNO} from {FRO} to {TO} is : {randint(222,555)} ")

t = train(89999)
t.book("glb","goa")
t.getstatus()
t.getfair("glb","goa")