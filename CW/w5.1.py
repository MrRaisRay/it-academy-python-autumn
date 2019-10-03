date = input("Input date:")
date = date.split('.')
template = "Today {y}/{m}/{d}"
print(template.format(y=date[0].split(),
                      m=date[1].split(),
                      d=date[2].split()))
