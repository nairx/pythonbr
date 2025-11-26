# file = open("./part7/students.txt","r")
# data = file.read()
# print(data)
# file.close()

# file = open("./part7/students.txt","r")
# for line in file:
#     print(line)
# file.close()

with open("./part7/students.txt") as file:
    for line in file:
        row = line.split(",")
        if int(row[1])>30:
            print(f"{row[0]}-{int(row[1])}-Pass")
        else:
            print(f"{row[0]}-{int(row[1])}-Fail")