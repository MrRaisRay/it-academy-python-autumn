def num_n_square(n=20):
    dtc = {i: i**2 for i in range(1, n + 1, 1)}
    return dtc

def char_count(s):
    dct = {el: s.count(el) for el in s}
    return dct

#print(num_n_square(int(input('Enter num: '))))
#print(char_count(' '.join(input('Enter el like str: ').split())))
