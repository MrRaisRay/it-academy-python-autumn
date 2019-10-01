s = input()
s = s.strip('')
s = s.replace(' ', '')
print(s)
if s == s[::-1]:
    print('Palindrome')
else:
    print('Not palindrome')
