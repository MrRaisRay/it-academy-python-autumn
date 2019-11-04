from HW6.Num_n_Square import char_count
from HW6.Num_n_Square import num_n_square
from HW6.MoreCountedWordFinder import more_counted_word


def runner(inner_lst):
    print(inner_lst)
    for el in inner_lst:
        if el == 'sqr':
            num_n_square(int(input('Enter num: ')))
            break
        elif el == 'charcout':
            char_count(' '.join(input('Enter el like str: ').split()))
            break
        elif el == 'mcw':
            more_counted_word()
            break
        elif not inner_lst:
            num_n_square(int(input('Enter num: ')))
            char_count(' '.join(input('Enter el like str: ').split()))
            more_counted_word()


s = input('Enter needed func: ').split()
runner(s)
