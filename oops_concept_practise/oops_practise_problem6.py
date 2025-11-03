'''6. Can you change the self-parameter inside a class to something else (say 
“harry”). Try changing self to “slf” or “harry” and see the effects. '''

from random import randint

class train:
    def __init__(slf,trainNO):
        slf.trainNO = trainNO

        

    def book(slf,FRO,TO):
        print(f"the trainno :{slf.trainNO}  booked from : {FRO} to : {TO}" )
    
    def getstatus(slf):
        print(f"the train {slf.trainNO} is running successfully on time")
    
    def getfair(slf,FRO,TO):
        print(f"the ticket fair in trainno :{slf.trainNO} from {FRO} to {TO} is : {randint(222,555)} ")

t = train(89999)
t.book("glb","goa")
t.getstatus()
t.getfair("glb","goa")