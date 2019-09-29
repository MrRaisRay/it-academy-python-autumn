Price = float(input('Enter price:'))
Count = int(input('Enter count:'))
Price *= Count
head = int(Price // 1)
tail = int(Price % 1 * 100)
print(f'Account in the amount of {head} rubles {tail} kopecks')
