n=int(input("enter the num of rows"))
space=5
for i in range(n,0,-1):
    for k in range(space):
        print(" ",end="")
    for j in range(1,i+1):
        print( "*" ,end=" ")
    print()
    space+=2
    