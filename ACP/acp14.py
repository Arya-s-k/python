radius = float(input("enter the radius"))

def calculate_circumference():
    if radius > 0:
        circumference = 2 * 3.14159265359 * radius
        print(circumference)
        return circumference
        
calculate_circumference()
