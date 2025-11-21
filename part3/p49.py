def mygen():
    for i in range(5):
        yield i
        
result = mygen()
# print(list(result))
# print(next(result))
# print(next(result))

for i in result:
    print(i)