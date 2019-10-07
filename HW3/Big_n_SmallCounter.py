data = str(input('Enter text: '))
small = big = 0
for i in data:
    if 'a' <= i <= 'z':
        small += 1
    elif 'A' <= i <= 'Z':
        big += 1
print(f'Small chars: {small} Big chars: {big}')
