def count_char(list1):
    count = 0
    for word in list1:
        if word[0] == word[-1]:
            count+=1
    print(list1)
    print("the number of times the first and last characters are same in the word is",count)
    
list1 =["civic","racer","camera","health"]
count_char(list1)