num = int(input('Enter number:'))
test = num
dopel = 0
while num / 10 > 0:
    dopel += num % 10
    num //= 10
    dopel *= 10
if test * 10 == dopel:
    print('palindrome')
else:
    print('not palindrome')
