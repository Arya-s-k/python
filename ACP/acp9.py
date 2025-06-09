base=int(input("enter the base "))
power=int(input("enter the power "))

res= 1

for i in range(power):
    res= base * power
    
print(f"the base {base} to the power {power}  is  {res}")