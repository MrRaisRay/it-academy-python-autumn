lst1 = [i + j for i in ['a', 'b'] for j in ['b', 'c', 'd']]
print(lst1)
print(lst1[::2])
lst2 = [str(i) + 'a' for i in range(1, 5, 1)]
print(lst2)
print(lst2.pop(1))
lst3 = lst2[::]
lst3.insert(1, 'a2')
print(str(lst3) + '\n' + str(lst2))
