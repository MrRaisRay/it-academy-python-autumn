data = input('Enter data>: ')
lst = data.split()
lst.sort()
print(lst)
i = 0
while 1:
    if lst.count(lst[i]) > 1:
        print(lst[i])
    i += lst.count(lst[i])
    if i >= len(lst):
        break
