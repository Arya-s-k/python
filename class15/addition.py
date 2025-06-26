def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b
    
ch = input("enter choice 1.addition \n 2.subtraction \n 3.multiplication \n 4.division \n enter your choice(1,2,3,4)")

n1=int(input("enter first number "))
n2=int(input("enter second number "))

if ch=="1":
    print(f"the sum of {n1} + {n2} is {add(n1,n2)}")
elif ch=="2":
    print(f"the difference of {n1} + {n2} is {sub(n1,n2)}")
elif ch=="3":
    print(f"the product of {n1} + {n2} is {mul(n1,n2)}")
elif ch=="4":
    print(f"the sum of {n1} + {n2} is {div(n1,n2)}")
else:
    print( "invalid")
