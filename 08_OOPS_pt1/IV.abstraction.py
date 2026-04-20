#abstraction is the 1st pillar of OOps
#Isme user ko sirf important chize dikhti h 
#unnecessary chize hide hojati h

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car Started..")

car1 = Car()
car1.start()


#isme clutch accelerator ye sb kuch output ni ayega 
#sirf car started print hoga