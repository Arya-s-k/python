my_set = {1, 2, 3}
print(my_set)

my_set = {1.0, "Hello", (1, 4, 4, 2, 1, 3)}
print(my_set)

my_set = {1, 2, 3, 4,4,5,9, 3, 2}
print(my_set)

my_set = set([1, 2, 3, 2])
print(my_set)

num_set = {0, 1, 3, 4, 5}
print("Original set:")
print(num_set)

print("After removing an element from the set:")
print(num_set)

num_set.remove(4)
print("After removing the number 4:")
print(num_set)