

try:
    n = int(input("enter the number"))
    print("The value of n is", n)
    
except ValueError as ex:
    print("The value error is", ex)