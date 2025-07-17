from datetime import date , time ,datetime

dt  = date.today()  
ti = datetime.now()

print("the date is ",dt) 
print("the current time is ",ti)
print("the date components are",dt.day,dt.month,dt.year)