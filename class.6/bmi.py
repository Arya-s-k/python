weight=float(input("enter your weight in kg: "))
height=float(input("enter your height in m: "))

BMI=weight / (height**2)

if BMI<18.5:
    print("you are underweight")
elif BMI<25:
    print("you are healthy")
elif BMI<30:
    print("you are overweight")
elif BMI<35:
    print("you are severly overweight")
elif BMI<40:
    print("you are obese")
else:
    print("you are extermly obese ")
   


