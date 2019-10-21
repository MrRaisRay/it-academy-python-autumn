country_count = int(input('Enter count of countries: '))
str_for_parse = []
main_dct = {}
for i in range(country_count):
    str_for_parse.append(input('Enter country and she own cityes: ').split())
    for string in str_for_parse[i]:
        if string == str_for_parse[i][0]:
            continue
        main_dct.update({string: str_for_parse[i][0]})
request_count = int(input('Enter how cities you search: '))
request_lst = []
for el in range(request_count):
    request_lst.append(input().upper())
print('-----------------------------------------')
for el in request_lst:
    print(main_dct[el])
