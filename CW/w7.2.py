def very_big_function(a, b = 0, *args, c, d=1, **kwargs):
    print(a, b, args, c, d, kwargs)


#very_big_function(1, 2, 3, 5, e=7)
very_big_function(1, 2, 3, b=8, c=5, e=7)
#very_big_function(c=1, 1, 2, 3)

def one_more(a, *, c):

#one_more(1,2)
one_more(3,c=0)