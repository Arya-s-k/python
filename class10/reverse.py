str1= input("enter a string")

rev= ""

for i in str1:
    rev= i + rev
    
print(f"the reverse of {str1} is {rev}")