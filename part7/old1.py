import os
os.chdir('C:/Users/nairx/test/MyDoc')
f=open("story.txt","r")
s = f.read()
print(s)
f.close()

#file is not closed after the operation
for line in open("myfile.txt"): 
    print(line, end="") 

#file will be closed automatically – predefined cleanup
with open("myfile.txt") as f: 
    for line in f: 
        print(line, end="") 