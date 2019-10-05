num = int(input('Enter number:'))
test = num
dopel = 0
while 1:
    dopel += num % 10
    num //= 10
    if num / 10 < 1:
        dopel = dopel * 10 + num % 10
        break
    dopel *= 10
if test == dopel:
    print('palindrome')
else:
    print('not palindrome')
