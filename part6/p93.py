from collections import ChainMap
d1 = {'a':5,'b':10}
d2 = {'c':7,'d':9}
d = ChainMap(d1,d2)
print(d)
print(d['a'])
print(d['c'])

for i,j in d.items():
    print(i,j)