# square
my_list = [5, 4, 3]

new_list = list(map(lambda num: num**2, my_list))
print(new_list)


# List sorting
a = [(0, 2), (4, 3), (2, -1), (3, -3)]
a.sort(key=lambda x: x[1])
print(a)
