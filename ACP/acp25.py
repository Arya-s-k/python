import random

def shuffle(string):
    templist = list(string)
    random.shuffle(templist)
    return ''.join(templist)

uppercaseletter1 = chr(random.randint(65,90)) 
uppercaseletter2 = chr(random.randint(65,90)) 
number = chr(random.randint(0,9))

password = uppercaseletter1 + uppercaseletter2 + number
password = shuffle(password)

print(password)