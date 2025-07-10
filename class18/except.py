

try:
    num1, num2 = eval(input("enter two numbers entered by commas"))
    
    res = num1 / num2
    
    print(res)
    
except SyntaxError as ex:
    
    print("the exception ", ex)
    
except ZeroDivisionError as ex:
    
    print("the exception ", ex)
    
except:
    
    print("error occured ")

else :
    print("no error occured")
