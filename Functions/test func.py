def positional(a, b, /, c=10):
    return a, b, c
    
def keyword(a, b, /, c, d):
    return a, b, c,d

def mixed(a, b, *, c, d=1):
    return a, b, c, d

def onlypositional(a, b, *, c, d):
    return a, b ,c

def onlykeyword(a, b, /, c, d):
    return a, b, c, d 

def onlymixed(a, b, c, d):
    return a, b, c, d

print(positional(7, 1, 20))
print(keyword(7, 1, d=9, c=2))
print(mixed(7, 1, c=10))
print(onlypositional(7, b=5,c=20, d=50))
print(onlykeyword(7,4, c=9, d=2))
print(onlymixed(b=10, a=60, c=10, d=2))