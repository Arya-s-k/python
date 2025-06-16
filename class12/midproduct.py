num=int(input("enter a value"))

str1= str(num)

len= len(str1)

if len%2==0:
    mid= int(len/2)-1
else:
    mid= int(len/2)
    
print(mid)
midproduct= int(str1[mid]) * int(str1[mid+1])
print("the mid product is ",midproduct)