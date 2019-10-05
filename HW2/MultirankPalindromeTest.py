num = int(input('Enter number:'))
test = num
dopel = 0
while 1:
    dopel += num % 10
    num //= 10
    if not num:
        print(num)
        break
    dopel *= 10
print(dopel)
if test == dopel:
    print('palindrome')
else:
    print('not palindrome')
