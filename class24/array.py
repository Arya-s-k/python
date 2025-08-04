import array as arr

a = arr.array("i",[1,2,3,4,5,5,5,6,5,5])
print("the array is",a)

print("the number of times 5 is repeated is ",a.count(5))

a.reverse
print("array reversed is ", str(a))