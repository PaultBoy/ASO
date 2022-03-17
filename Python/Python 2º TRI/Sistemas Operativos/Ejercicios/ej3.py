from encodings import utf_8
import os
import sys
import shutil
if sys.platform == "win32":
    try:
        path = os.path.join(os.environ['temp'],"La_Palma")
        os.makedirs(path)
        files = []
        with open("./La_Palma.txt","r",encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                stripped_line=line.strip()
                stripped_line=stripped_line + ".mp3"
                files.append(stripped_line)
    
            for file in files:
                os.system("powershell New-Item -Path "+ path +" -Name '"+file+"' -ItemType 'file'")
    except FileExistsError:
        pathDel = os.path.join(os.environ['temp'],"La_Palma")
        shutil.rmtree(pathDel)
    
else:
    try:
        path = os.path.join("/tmp","La_Palma")
        os.makedirs(path)
        files = []
        with open("./La_Palma.txt","r",encoding="utf_8") as f:
            lines = f.readlines()
            for line in lines:
                stripped_line=line.strip()
                stripped_line=stripped_line + ".mp3"
                files.append(stripped_line)
        for file in files:
            path = os.path.join("/tmp","La_Palma",file)
            os.system("touch "+path)
    except FileExistsError:
        pathDel = os.path.join("/tmp","La_Palma")
        shutil.rmtree(pathDel)