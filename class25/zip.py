list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']

mylist = list(zip(list1,list2))
print(mylist)

a = (1,2,3,4,5)
b= (100,200,300,400,500)

rev = (list(zip(a,b[::-1])))
print(rev)

stock = ['infosys','reliance','jio']
price = [1234,456,790]

mydict = {stock:price for stock,price in zip(stock,price)}
print(mydict)