dict_ = eval(input("enter a dictionary : "))

k = 2
count = 0


for key in dict_.keys():
    
    if k == dict_[key]:
        count += 1

print(f"the dictionary which has {k} frequency is {count}")