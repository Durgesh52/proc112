import os
import shutil

source="C:/Users/HP/Downloads"
dest="F:/dest"

list_of_files=os.listdir(source)

for s in list_of_files:
    name,extension = os.path.splitext(s)
  
    if(extension==""):
        continue
    if extension in[".xlx",".pdf",".doc" ]:
        path1=source +  "/" +s
        path2=dest+ "/" +"pdfs"
        path3=dest+ "/" +"pdfs" + "/" + s
        if os.path.exists(path2):
            print("Moving ",s)
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            print("Moving ",s)
            shutil.move(path1,path3)
    

