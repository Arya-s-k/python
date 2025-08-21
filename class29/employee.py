class person:
    def __init__(self,name,id):
        self.id = id
        self.name = name
    def display_person(self):
        print("my name is ",self.name)
        print("my id is ",self.id)
class employee(person):
    def __init__(self,salary,post, name, id):
        self.salary = salary 
        self.post = post
        person.__init__(self,name,id)
    def display_emp(self):
        self.display_person()
        print("my post is ",self.post)
        print("my salary is ",self.salary)
        
employee1 = employee(5000,"technician","ram","129")
employee1.display_emp()