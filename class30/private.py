class method:
    __mypriv = 89 

    def __privatemethod(self):
        print("this is the private method")
    def publicmethod(self):
        print("the private variable is",self.__mypriv)
obj1 = method()  
obj1.publicmethod()
        