class parrot:
    species = "Macaw"
    
    def __init__(self,name,age):
        self.name = name
        self.age = age 
        
parrot1 = parrot("rob",2)
parrot2 = parrot("jos",3)

print("my specis is ",parrot1.species) 
print("my name is ",parrot1.name)
print("my age is ",parrot1.age)       


print("my specis is ",parrot2.species) 
print("my name is ",parrot2.name)
print("my age is ",parrot2.age)       