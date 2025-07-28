weather = (0,0,1,0,0,1,0,0,1)

s=0
r=0

for i in weather:
    if i == 0:
        s +=1
    else :
        r += 1
        
if s > r :
    print("it is sunny weather")
else :
    print ("it is rainy weather ")