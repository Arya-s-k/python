def hotel (nights):
   return nights * 200

def plane(city):
    if city == "mumbai":
        return 500
    elif city == "banglore":
        return 250
    elif city == "delhi":
        return 400
    elif city == "chennai":
        return 450
    
def car(day):
    if day >= 7:
        return day *40 -50
    elif day >= 3:
        return day * 40 - 20
    else :
        return day * 40
    
def trip_cost(city,day,nights,spending):
    return plane(city) + hotel(nights) + car(day) + spending()

print("the total cost is ",trip_cost("mumbai",7,6,500))