from functools import reduce
score = [45,75,90,10]
def f1(x,y):
    return x+y

result = reduce(f1,score)
print(result)

# score = [45,75,90,10]
# def f1(x):
#     return x>40

# result = filter(f1,score)
# print(list(result))


# def f1(x):
#     return x+1

# result = map(f1,[2,5,3])
# print(list(result))