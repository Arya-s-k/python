class bird :
    def __init__(self):
        print("bird is ready")
    def fly(self):
        print("bird can fly")
        
        
class penguin(bird):
    def __init__(self):
        super().__init__()
        print("penguin is ready")
        
    def run(self):
        print("penguin runs ")
        
    
       
peggy = penguin()
peggy.run()
peggy.fly()
        

    