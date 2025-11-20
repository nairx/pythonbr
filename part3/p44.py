names = ["John","Amy","Cathy","Peter","Mike"]
score = [45,65,78,90]
result = zip(names,score)
print(list(result))

for i,j in zip(names,score):
    print(i,j)