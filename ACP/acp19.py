import calendar

for i in range(13):
    res = calendar.month_name[i]
    print("Month Name : " + str(res))

n=int(input("write month number"))
print(calendar.month(2025, n))