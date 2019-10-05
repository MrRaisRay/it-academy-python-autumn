lst = input('Enter el like str: ').split()
dct = {el: lst.count(el) for el in lst}
print(dct)

