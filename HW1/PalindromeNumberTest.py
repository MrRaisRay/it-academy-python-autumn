num = input('Enter yout test number:')
if num == num[::-1]:
    print('Number %s is palindrome' % num)
else:
    print('Number %s is not palindrome' % num)
