num = int(input('Enter number:'))
a = b = 1
for i in range(num):
    print(b)
    b += a
    if i + 1 >= num / 2 + 0.5:
        break
    print(a)
    a += b
