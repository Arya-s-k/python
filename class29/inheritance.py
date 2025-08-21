class vehicle :
    def __init__(self,name,maxspeed,mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage
        
    def display(self):
        print("the name of the vechicle is ",self.name)
        print("the name of the maxspeed is ",self.maxspeed)
        print("the name of the mileage is ",self.mileage)
        
class bus(vehicle):
    pass

bus1 = bus("scania","130km/hr","10km/l")
bus1.display()
