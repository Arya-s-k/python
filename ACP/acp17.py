def check_age():
    while True:
        try:
            age = int(input("Please enter your age: "))
            if 0 <= age <= 120:
                print(f"You entered: {age} years old.")

                
                if age % 2 == 0:
                    print("Your age is an EVEN number.")
                else:
                    print("Your age is an ODD number.")
                break  
            else:
                print("Error: Age is written wrong ")

        except ValueError:
            
            print("Error: no decimal places")
            
        except Exception as x:
            print("An unexpected error occurred:")

check_age()