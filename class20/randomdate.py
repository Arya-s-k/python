import random
import datetime

def random_date(start,end):
    random_sec= random.randint(0,int((end -start).total_seconds()))
    
    rdate = datetime.timedelta(seconds=random_sec)
    
    return start+rdate

start = datetime.datetime(2020,1,1)
end = datetime.datetime(2021,1,1)

random_date =random_date(start,end)

print(f"random date between {start} and {end} is {random_date}")