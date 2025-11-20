score = [65,90,30,50]
result = [i>40 for i in score]
if any(result):
    print("Promoted")
else:
    print("Failed")

# for i in score:
#     if i<40:
#         print("Failed")
#         break
# else:
#     print("Promoted")







# result = [True,False,True,False]
# print(any(result))
# print(all(result))