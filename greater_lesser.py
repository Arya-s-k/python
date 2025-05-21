num= int(input("enter a number :"))
if num<15:
    print(f"{num}is less than 15")
    print("i'm in if block")
else:
    print(f"{num} is greater than 15")
    print("im in else block")
print("im outside both blocks")