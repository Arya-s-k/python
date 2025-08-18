class dog:
    species = "golden retriver "
    
    def __init__(self,name,age):
        self.name = name
        self.age = age 
        
dog1 = dog("gopi",2)
dog2 = dog("ruby",5)

print("my specis is ",dog1.species) 
print("my name is ",dog1.name)
print("my age is ",dog1.age)       


print("my specis is ",dog2.species) 
print("my name is ",dog2.name)
print("my age is ",dog2.age)       