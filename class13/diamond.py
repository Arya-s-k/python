n=int(input("enter num of rows"))
space=30

for i in range(1,n+1,2):
    for j in range(space):
        print(" ", end="")
    for k in range(1,i+1,1):
        print(k,end="")
    print( )
    space-=1

space+=2    
for i in range(n-2,0,-2):
    for j in range(space):
        print(" ", end="")
    for k in range(1,i+1,1):
        print(k,end="")
    print( )
    space+=1