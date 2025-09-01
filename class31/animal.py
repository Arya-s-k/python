from abc import ABC,abstractmethod
class animal(ABC):
    
    @abstractmethod
    def move(self):
        pass
    
class human:
    def move(self):
        print("i move with walking")

class snake:
    def move(self):
        print("i move by slithering")

class fish :
    def move(self):
        print("i move by swimming")
    
    
h1=human()
h1.move()
s1=snake()
s1.move()
f1=fish()
f1.move()