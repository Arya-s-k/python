def flip_flop(t):
    s = 0
    e = len(t) - 1
    while s <= e:
        if t[s] != t[e]:
            return False
        s+=1
        e-=1
    return True

t=(1,2,3,3,2,1)
flag = flip_flop(t)
if flag:
    print("the tuple is flip flop")
else:
    print("the tuple is not a flip flop")
           
            