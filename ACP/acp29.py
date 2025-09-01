class reverstr:
    def __init__(self, phrase):
        self.phrase = phrase

    def rev(self):
        word_list = self.phrase.split()
        word_list.reverse()
        
        new_rev = " ".join(word_list) 
        print("the original string is \n", self.phrase)
        print("the reverse string is \n", new_rev)

r1 = reverstr("all that glitters is not gold")
r1.rev()