num = int(input('Enter yout test number:'))
check = 0
for i in range(num+1):
    if i == 0:
        continue
    if num % i == 0:
        check = check + 1
if check > 2:
    print('Number %s is not prime' % num)
else:
    print('Number %s is prime' % num)
