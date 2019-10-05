string = input('Enter str').lower()
i=0
for el in string:
   if 'a' < el < 'z':
       i += 1
print(i)
