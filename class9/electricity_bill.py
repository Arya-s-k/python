units=int(input("enter units consumed"))

if units<50:
    e_b= units * 2.60 + 25
elif units<100:
    e_b=units * 3.60 + 35
elif units<200:
    e_b=units * 5.26 + 45
else :
    e_b=units * 8.45 + 75

print("the electricity bill is ",e_b)
