from abc import ABC,abstractmethod

class abstractclass:
    def printex(self,x):
        print("the value of x is ",x)
        
    @abstractmethod
    def abcmethod(self):
        pass
    
class inh(abstractclass):
    def abcmethod(self):
        print("i am inherited class")
        
obj1 = inh()
obj1.printex(100)
obj1.abcmethod()