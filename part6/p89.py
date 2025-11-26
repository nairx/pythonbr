from collections import Counter
names = ["John","Cathy","John","Amy"]
mycounter = Counter(names)
print(mycounter)
print(mycounter.most_common(1))