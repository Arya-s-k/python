num=int(input("enter a number to check if it is an armstrong number"))
temp=num
sum=0

while temp != 0:
    digit = temp % 10
    sum +=  digit**3
    temp //= 10 
    
if num == sum:
    print(f"{num} is an armstrong number ")
else:
    print(f"{num} is not an armstrong number ")