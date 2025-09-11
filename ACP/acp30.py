class BMW:
    def speed(self):
        print("the speed is 120 km/h")
    def type(self):
        print("it is an AWD")
        
class ferrari:
    def speed(self):
        print("the speed is 115 km/h")
    def type(self):
        print("it is a RWD")

b1=BMW()
f1=ferrari()

for i in (b1,f1):
    i.speed()
    i.type()


       