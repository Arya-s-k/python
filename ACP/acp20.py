list_ = [12,34,90,77]

start = 0
end = 4
a = []
even = []
odd = []

for i in list_:
    sq = i * i
    a.append(sq)
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(a)
print(even)
print(odd)