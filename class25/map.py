list1 = [1,2,3,4]
list2 = [5,6,7,8]

sum = list(map(lambda x , y : x + y , list1,list2))
print(sum)

a = [36,21,54,76]

def sqr(x):
    return x*x

sq = (list(map(sqr,a)))
print("the squares of the list a is ")
print(sq)