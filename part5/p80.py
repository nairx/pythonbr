import os
from datetime import datetime
dt = datetime.now()
foldername = dt.strftime("%Y%m%d")
if not os.path.exists(foldername):
    os.mkdir(foldername)
os.chdir(foldername)
filename = dt.strftime("%Y%m%d%H")
# if not os.path.isfile(filename+".txt"):
file = open(filename+".txt","a")
str = dt.strftime("%Y%m%d%H%M%S")
file.write(str+"- Hello World\n")
file.close()
data = open(filename+".txt","r")
print(data.read())


    
