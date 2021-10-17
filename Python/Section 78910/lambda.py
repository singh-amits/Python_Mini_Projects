from functools import reduce
my_list = [1, 2, 3]

print(list(map(lambda item: item*2, my_list)))
print(my_list)

# filter
print(list(filter(lambda item: item % 2 != 0, my_list)))\

# reduce
print(reduce(lambda acc, item: acc+item, my_list))
