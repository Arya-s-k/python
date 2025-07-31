codingal_dict = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}

k = 2
count = 0

for key in codingal_dict.keys():
    print(key)
    if k == codingal_dict[key]:
        count+=1
print (f"the dictionary which has {k} frequency is {count}")        