Price = int(input('Enter price:'))+int(input())*0.01
Count = int(input('Enter count:'))
Price *= Count
head = Price // 1
tail = Price % 1 * 100
print(f'Account in the amount of {head} rubles {tail} kopecks')
