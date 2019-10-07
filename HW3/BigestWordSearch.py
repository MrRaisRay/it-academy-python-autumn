data = str(input('Enter some text: '))
chars = ". , ; : ' ! & $ % ( ) + - * / =".split()
for c in chars:
    data.replace(c, '')
data = data.split()
checker = 0
for i in data:
    if len(i) > checker:
        checker = len(i)
        target = i
print(target)
