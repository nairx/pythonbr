import os
from datetime import datetime
d = datetime.now()
# from time import sleep
# print(os.listdir())
# os.chdir("part1")
# print(os.listdir())
# os.chdir("..")
# print(os.listdir())
# os.mkdir("newfolder")
# print(os.listdir())
# sleep(5)
# os.rmdir("newfolder")
# print(os.listdir())
# os.makedirs("newfolder/folder1")
# os.removedirs("newfolder/folder1")
folder = d.strftime("%Y%m%d%H%M%S")
os.mkdir(folder)
