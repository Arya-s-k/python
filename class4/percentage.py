#percentage calculation
math=int(input("enter your math marks:"))
science=int(input("enter your science marks:"))
english=int(input("enter your english marks:"))
sst=int(input("enter your sst marks:"))
sum=math+science+english+sst
print("your total number of marks scored is = ",sum)
percent=(sum/400)*100
print("Your percentage is = ",percent,"%")