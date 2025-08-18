
class iostring :
    
    def __init__(self):
        self.str1 = ""
    def getstring(self):
        self.str1 = input("enter a string :")
    def printstring(self):
        self.str1 = print("the uppercase of the given string is ",self.str1.upper())
        
obj1 = iostring()
obj1.getstring()
obj1.printstring()