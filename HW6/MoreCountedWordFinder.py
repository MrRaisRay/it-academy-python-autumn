def more_counted_word():
    lst = input('Enter el like str: ').lower().split()
    dct = {el: lst.count(el) for el in lst}
    finder = max(dct.values())
    print(finder)
    res_list = []
    print(type(res_list))
    for i in dct.keys():
        if dct[i] == finder:
            res_list.append(i)
    res_list.sort()
    print(dct)
    print(res_list)

more_counted_word()