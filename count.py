#program to count number of notes to give
a=int(input("enter your amount:"))
note_100=a//100
note_50=(a%100)//50
note_10=((a%100)%50)//10
print("100 rupee notes",note_100)
print("50 rupee notes",note_50)
print("10 rupee notes",note_10)