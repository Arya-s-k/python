class pairofelements :
    def twosum(self,tuple1,target):
        lookup = {}
        sum = 0
        
        for index,value in enumerate(tuple1):
            
             sum = sum + value 
             if sum <= target:
                 lookup[index] = sum
             else :
                print("the position of the element upto 100 is",index)
                print(lookup)
                return
        
obj1 = pairofelements()
tuple1 = (10,20,30,40,50,60,70,80,90,100)
target = 100
obj1.twosum(tuple1,target)
                             
        