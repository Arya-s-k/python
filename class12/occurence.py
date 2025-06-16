word = input("enter a string ")
char = input("enter a character ")
count= 0
for i in word:
    if i == char:
        count += 1 
        
print("the number of occurence of the char is ",count)
    