import os
from datetime import datetime
dt = datetime.now()
folder = dt.strftime("%Y%m%d")
# if os.path.exists(folder):
#     print("Folder Already Exists")
# else:
#     os.mkdir(folder)

# if os.path.isfile(folder):
#     print("Folder Already Exists")
# else:
#     os.mkdir(folder)
    
# if os.path.isdir(folder):
#     print("Folder Already Exists")
# else:
#     os.mkdir(folder)

os.chdir("part5")
# os.remove("file1.txt")
# os.rename("file1.txt","newfile.txt")
os.replace("file1.txt","newfile.txt")

