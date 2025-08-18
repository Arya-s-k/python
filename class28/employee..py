class employee :
    
    def __init__(self):
        print("employee created ")
    def __del__(self):
        print("empolyee deleted")
        
obj1 = employee()
del(obj1)
obj2 = employee()