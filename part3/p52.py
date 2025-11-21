import sys
list = [i for i in range(100000)]
gen = (i for i in range(100000))

print(type(list))
print(type(gen))

print(sys.getsizeof(list),"bytes")
print(sys.getsizeof(gen),"bytes")

