class flashcard:
    def __init__(self,word,meaning):
        self.word = word 
        self.meaning = meaning
        
    def __str__(self):
        return f"{self.word} ({self.meaning})"
    
flash = []
print("welcom to flashcard application")
while True:
    word = input("enter a word")
    meaning = input("enter the meaning of the word")
    flash.append(flashcard(word,meaning))
    ch = input("do you want to countinue (y/n)")
    if ch.lower() == "n":
        break
    
print("flashcards are :")
for i in flash:
    print(">",i)