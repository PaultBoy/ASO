import subprocess

import os

import sys

import shutil
#Nombre de las carpetas
folders = ["ASO","Python", "Powershell", "Bash"]

if sys.platform == "win32":

    paths = []

    for i in range(len(folders)):

        if folders[i] == "ASO":
            #Añadir cada ruta al array paths, para proceder a añadirlas, creando ASO como la carpeta raíz
            paths.append(os.path.join(os.environ['temp'],folders[i]))

        else:

            paths.append(os.path.join(os.environ['temp'],folders[0],folders[i]))

    try:

        for j in range(len(paths)):

            os.makedirs(paths[j])

            if j >= 1:

                os.system("powershell New-Item -Path "+ paths[j] +" -Name 'helloworld' -ItemType 'file'")
        #Al mostrar el árbol completo, volverá a pasar por todos los elementos por pantalla
        subprocess.run(["powershell ","gci","-recurse", os.path.join(os.environ['temp'],"ASO")])
    except FileExistsError:
        print("Directorios ya creados")
        print("Procedemos a borrarlos")
        shutil.rmtree(paths[0])

    

elif sys.platform == 'linux':

    pathsLin = []

    for i in range(len(folders)):

        if folders[i] == "ASO":

            pathsLin.append(os.path.join('/tmp/',folders[i]))

        else:

            pathsLin.append(os.path.join('/tmp/',folders[0],folders[i]))

    try:

        for j in range(len(pathsLin)):

            os.makedirs(pathsLin[j])

            pathTemp = os.path.join(pathsLin[j],"helloworld")

            if j >= 1:

                subprocess.run(["touch", pathTemp])
        subprocess.run(['ls','-laR','/tmp/ASO'])
    except FileExistsError:
        print("Directorios ya creados")
        print("Procedemos a borrarlos")
        shutil.rmtree(pathsLin[0])

    

