data = str(input()).replace(' ', '')
targetstr = ''
trash = ''
for i in data:
    if trash.find(i) == -1:
        targetstr += i
        trash += i
print(targetstr)
