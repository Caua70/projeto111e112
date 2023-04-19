import os 
import shutil

from_dir = "C:/Users/User/Desktop/downloads"
to_dir = "C:/Users/User/Desktop/arquivos_documentos"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for k in list_of_files:
    name, extencion = os.path.splitext(k)

    if extencion == "":
        continue


    if extencion in [".doc",".docx",".pdf",".txt"]:
        path1 = from_dir + "/" + k
        path2 = to_dir + "/" + "textfile"
        path3 = to_dir + "/" + "textfile" + "/" + k 

    if os.path.exists(path2):
        shutil.move(path1, path3)

    else: 
        os.makedirs(path2)
        shutil.move(path1 , path3) 
