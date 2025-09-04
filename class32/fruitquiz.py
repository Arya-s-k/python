import random
class friutquiz:
    def __init__(self):
        self.fruits = {"apple":"red",
                       "bannana":"yellow",
                       "orange":"orange",
                       "water melon":"green"
        }
        
    def quiz(self):
        while True:
            fruit,colour = random.choice(list(self.fruits.items()))
            print("what is the colour of ",fruit)
            c= input()
            if c == colour:
                print("correct answer")
            else:
                print("wrong answer")
            ch = input("do you want to continue (y/n):")
            if ch.lower() == "n ":
                break

fq = friutquiz()
fq.quiz()
                