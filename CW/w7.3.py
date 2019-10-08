def print_func(a, b, *, c, d):
    print(a, b, c, d)


pos_arg = [1, 2]
pos_tuple = (1, 2, 3, 4)
named_dict = {'c': 5, 'd': 7, 'f': 8}
#print_func(*pos_arg, **named_dict)
print_func(*pos_tuple, **named_dict)
