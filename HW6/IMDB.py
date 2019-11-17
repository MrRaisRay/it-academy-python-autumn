imdb = open('./ratings.list', 'r')
file_str = imdb.read()
imdb.close()
start_point = file_str.find('      00000')
end_point = file_str.find('\n\nBOTTOM 10')
top_250 = file_str[start_point:end_point:]
lst_top_250 = top_250.split('\n')
for i in range(len(lst_top_250)):
    lst_top_250[i] = lst_top_250[i].lstrip()
dct_top_250 = {}
top250_str = ''
dct_ratings = {}
dct_years = {}
for el in lst_top_250:
    el = el.replace('  ', ' ')
    el = el.replace('  ', ' ')
    inner_start_point = el.find('.') + 3
    inner_end_point = el.find('(')
    top250_str += el[inner_start_point:inner_end_point - 1:] + '\n'
    str_info = el.replace(el[inner_start_point:inner_end_point - 1:], '')
    lst_info = str_info.split()
    lst_info[3] = lst_info[3].replace('(', '').replace(')', '')
    if dct_ratings.get(lst_info[2]) is None:
        dct_ratings[lst_info[2]] = 1
    else:
        dct_ratings[lst_info[2]] += 1
    if dct_years.get(lst_info[3]) is None:
        dct_years[lst_info[3]] = 1
    else:
        dct_years[lst_info[3]] += 1
open('./top250_movies.txt', 'w').write(top250_str)
str_ratings = ''
str_years = ''
for rate in range(80, 100,):
    str_ratings += str(float(rate) / 10)
    str_ratings += '+'
    for key in dct_ratings.keys():
        if float(rate) / 10 == float(key):
            str_ratings += '+' * (dct_ratings[key] + 1)
            break
    str_ratings += '\n'
open('./ratings.txt', 'w').write(str(str_ratings))
for year in range(1900, 2019,):
    str_years += str(year)
    str_years += '+'
    for key in dct_years.keys():
        if str(year) == key:
            str_years += '+' * (dct_years[key] + 1)
            break
    str_years += '\n'
print(str_years)
open('./years.txt', 'w').write(str(str_years))

