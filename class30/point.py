class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x},{self.y})"
    
p1 = point(100,104)
print(p1)
    