speed1=int(input("enter speed1 : "))
speed2=int(input("enter speed2 : "))
speed3=int(input("enter speed3 : "))

avg=(speed1+speed2+speed3)/3
print(avg)

if speed1 < avg:
    print("cyclist 1 is slower than average")
if speed2 < avg:
    print("cyclist 2 is slower than average")
if speed3 < avg:
    print("cyclist 3 is slower than average")
