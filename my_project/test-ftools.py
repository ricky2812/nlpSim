from functional import my_map, my_filter, my_reduce

def rev(x):
    return 6 - x

def not_three(x):
    return x != 3

def stick(x, y):
    return x * 10 + y

numbers1 = [1, 2, 3, 4, 5]
print(numbers1)

numbers2 = my_map(rev, numbers1)
print(numbers2)

numbers3 = my_filter(not_three, numbers2)
print(numbers3)

number = my_reduce(stick, numbers3)
print(number)
