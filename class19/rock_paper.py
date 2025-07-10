import random

list1=['rock','paper','scissors']

while True:
    comp = random.choice(list1)
    user = input("enter rock , paper, scissors:")
    
    if user.lower() == comp.lower():
        print("it is a tie ")
    elif (user == "rock" and comp == "scissors") or (user == "paper" and comp == "rock" ) or (user == "scissors" and comp == "paper"):
        print("you win")
    else:
        print("i win")
    ch = input("do you want to play (y/n)")
    if ch == "n":
        break
    