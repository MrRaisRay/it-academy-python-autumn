def char_sum(a=0):
    s = 0
    while 1:
        s += a % 10
        if not a:
            break
        a = a // 10
    print(s)


char_sum(int(input()))