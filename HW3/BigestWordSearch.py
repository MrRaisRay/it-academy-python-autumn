data = str(input('Enter some text: ')).replace(',', '').replace('-', '').replace(':', '').replace('.', '').split()
checker = 0
for i in data:
    if len(i) > checker:
        cheker = len(i)
        target = i
print(target)
