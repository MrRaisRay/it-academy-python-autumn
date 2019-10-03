rubles = int(input('Enter rubles: '))
kopecks = int(input('Enter kopecks: '))
count = int(input('Enter count: '))
price = (rubles + kopecks * 0.01) * count
head = int(price // 1)
tail = int(price % 1 * 100)
print(f'Account in the amount of {head} rubles {tail} kopecks')
