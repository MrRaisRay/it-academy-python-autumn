num = int(input('enter number:'))
a = b = 1
#print(a)
#print(b)
#num -= 2
for i in range(num):
    if i == num // 2:
        break
    print(b)
    b += a
    print(a)
    a += b

