medical_clause=input("Y or N")
attendance=int(input("tell attendance"))

if medical_clause=="N":
    if attendance > 75:
        print("you are eligible to write exam")
    else:
        print("you are not eligible ")  
else:
    print("you are eligible")
    
    
    