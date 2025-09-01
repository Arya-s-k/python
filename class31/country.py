class india:
    def capital(self):
        print("the capital of india is new delhi")
    def language(self):
        print("the language spoken here is hindi")
    def currency(self):
        print("curency is rupee")
class usa :
    def capital(self):
        print("the capital is is washington D .C")
    def language(self):
        print("the language spoken here is english")
    def currency(self):
        print("the currency is dollar")
        
i1 = india()
u1 = usa()

for i in (i1,u1):
    i.language()
    i.capital()
    i.currency()
    