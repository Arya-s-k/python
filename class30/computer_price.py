class computer :
    def __init__(self):
        self.__maxprice = 900
    def pprice(self):
        print("the max price is ",self.__maxprice)
    
    def setmaxprice(self,price):
        self.__maxprice = price
        
computer1 = computer()        
computer1.pprice() 
computer1.setmaxprice(1200)
computer1.pprice() 
