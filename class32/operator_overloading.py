class A :
    def __init__(self,a):
        self.a = a
        
    def __lt__(self,other):
        if (self.a < other.a):
            return "obj1 is less than obj2"
        else:
            return "obj1 is greater than obj2"
        
    def __el__(self,other):
        if (self.a == other.a):
            return "obj1 is equal to obj2"
        else:
            return "obj1 is not equal to obj2"
        
obj1 = A(10)
obj2 = A(12)

print(obj1<obj2)
print(obj1 == obj2)
         