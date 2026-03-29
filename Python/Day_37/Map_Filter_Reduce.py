def cube(x):
    return x ** 3

l = [1,2,3,4,5,6,7,8,9,10]

def filter_even(x):
    return x % 2 == 0


# Map
new_l = list(map(cube, l))
print(new_l)

# Filter
filtered_l = list(filter(filter_even, l))
print(filtered_l)

# Reduce
from functools import reduce

def add(x, y):
    return x + y

def max_func(x, y):
    return x if x > y else y

total_sum = reduce(add, l)
max_value = reduce(max_func, l)
print(total_sum)
print(max_value)

# zip
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))
print(zipped)
for a, b in zipped:
    print(f"{a} - {b}")
