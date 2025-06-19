
decimalnum = int(input("enter decimal Number  : "))
binarynum = 0
num = 1
while decimalnum>0:
    rem = decimalnum%2
    binum = binarynum+(rem*num)
    num = num*10
    decimalnum = int(decimalnum/2)

print("binary number = ", binum)