import os
from datetime import datetime
dt = datetime.now()
os.chdir("part5")
f = open("file1.txt","a")
str = dt.strftime("%Y%m%d%H%M%S")
txt = str + "-Hello World\n"
f.write(txt)
print(os.listdir())