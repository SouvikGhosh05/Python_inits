string = "11-13,12-14,13-15"

Dict = dict((x, y) for x, y in (element.split('-') for element in string.split(',')))
# elements are '11-13','12-14','13-15'

print(Dict)
for element in string.split(','):
    for x,y in element.split('-'):
        print(x,y,end=' ')