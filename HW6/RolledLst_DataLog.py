import os
import sys


def loger(func):
    def wrapper(dec_lst):
        print(func(dec_lst))
        log = open('RolledLst.log', 'r').read()
        log += func(dec_lst) + '\n'
        open('RolledLst.log', 'w').write(log)
    return wrapper


@loger
def get_ranges(inner_lst):
    indicator = 0
    result_str = ''
    for i in range(len(inner_lst)):
        if i + 1 == len(inner_lst) and indicator == 1:
            result_str += '-' + str(inner_lst[i])
            break
        elif i + 1 == len(inner_lst) and indicator == 0:
            result_str += str(inner_lst[i])
            break
        elif inner_lst[i] - 1 != inner_lst[i - 1] and inner_lst[i] + 1 != inner_lst[i + 1]:
            result_str += str(inner_lst[i]) + ', '
        elif inner_lst[i] - 1 != inner_lst[i - 1] and inner_lst[i] + 1 == inner_lst[i + 1]:
            result_str += str(inner_lst[i])
            indicator = 1
        elif inner_lst[i] + 1 == inner_lst[i + 1]:
            indicator = 1
            continue
        elif inner_lst[i] + 1 != inner_lst[i + 1]:
            result_str += '-' + str(inner_lst[i]) + ', '
            indicator = 0
    return result_str


lst = input().split()
if not lst:
    print('Bad data')
    os.execl(sys.executable, sys.executable, *sys.argv)
for i in range(len(lst)):
    lst[i] = int(lst[i])
print("Inputed data is " + str(lst))
for i in range(len(lst) - 1):
    if lst[i] >= lst[i + 1]:
        print('Bad data')
        os.execl(sys.executable, sys.executable, *sys.argv)
get_ranges(lst)
