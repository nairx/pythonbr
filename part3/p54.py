# import sys
# list = [i for i in range(10)]
# print(type(list))
# print(list[0])
# gen = (i for i in range(10))
# print(type(gen))
# print(sys.getsizeof(list))
# print(sys.getsizeof(gen))

# # for i in list:
# #     print(i)
    
# for i in gen:
#     print(i)

# list = [5,8,6,4,3]
# gen = iter(list)
# print(type(list))
# print(type(gen))

def mygen():
    for i in range(10):
        yield i
        
gen = mygen()
print(type(gen))
