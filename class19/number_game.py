import random

comp= random.randint(10,20)

while True :
    user = int(input("enter a number :"))
    
    if comp==user:
        print("congratulations")
    else:
        print("try again")
        break
    print("do you want another chance (y/n)")
    x=input("")
    if x=="n":
        break