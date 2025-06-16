upper = int(input (" enter the uppper limit "))
lower = int(input (" enter the lower  limit "))

for i in range(lower,upper+1):
        for j in range(2,i):
            if i % j == 0:
                break;
            else:
                print(i)
        


        

