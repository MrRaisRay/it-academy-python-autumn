def fun_func(a):
    print(a)


fun_func([1, 2, 3, ])
fun_func({1: 2, 3: 4})
fun_func(4)
fun_func('str"ing')


def strange_func():
    print('strange')


fun_func(strange_func)
fun_func(strange_func())
