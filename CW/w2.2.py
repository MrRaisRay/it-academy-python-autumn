var = int(input('Enter number:'))
if var % 2 != 0:
    print('oho')
else:
    if var > 0:
        print('normal')
    elif var < 0:
        print('not enough')
    else:
        print('null')
