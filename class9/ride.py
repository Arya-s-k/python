print("customize your ride")
print("choose 1 for car")
print("choose 2 for bike")
ch=int(input("select the ride"))

if ch==1:
    print("what type of car do you want 1.sedan \n 2.xuv\n")
    ch2=int(input("selcet type"))
    if ch2==1:
        print("you have selected sedan")
    elif ch2==2:
        print("you selected xuv")
    else :
        print("wrong input")
elif ch==2:
    print("what type of bike do you want 1.scooty \n 2.pulsar\n")
    ch2=int(input("selcet type"))
    if ch2==1:
        print("you have selected scooty")
    elif ch2==2:
        print("you selected pulsar")
    else :
        print("wrong input")
else:
    print("wrong input")
