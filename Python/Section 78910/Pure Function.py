# 1. def multiply_by2(li):
#new_list = []
# for item in li:
# new_list.append(item*2)
# return new_list


#print(multiply_by2([1, 2, 3]))

# Map, Filter, Zip and Reduce

# 1. my_list = [1, 2, 3]
# def multiply_by2(item):
#   return item*2

#print(list(map(multiply_by2, my_list)))
# print(my_list)

# 2. my_list = [1, 2, 3]

# def multiply_by2(item):
# return item*2


# def only_odd(item):
#   return item % 2 != 0


#print(list(filter(only_odd, my_list)))
# print(my_list)

my_list = [1, 2, 3]
your_list = [10, 20, 30]


def multiply_by2(item):
    return item*2


def only_odd(item):
    return item % 2 != 0


print(list(zip(my_list, your_list)))
print(my_list)
