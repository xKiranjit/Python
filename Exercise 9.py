import os
import shutil

# print(os.listdir("c:/temp"))
for file in os.listdir("c:/temp python"):
    ext = file[file.find("."):]
    if ext == '.txt':
      shutil.move("c:/temp python/" + file, "c:/temp python/dest/" + file)
      print("move " + file)
    else:
        print(file + " not moved")