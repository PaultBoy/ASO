import pandas, subprocess

df_dptos= pandas.read_csv("/root/Departamentos.csv")
df_users= pandas.read_csv("/root/UsuariosSamba.csv")

lst_dptos=df_dptos.values.tolist()
lst_users=df_users.values.tolist() 

""" for item in lst_dptos:
    #print(item[0])
    #Crear grupos para cada DPTOP con el elemento 0 de un csv
    subprocess.run(['samba-tool','group','add',item[0]])
    #Crear una OU con el nombre de cada DPTO. + para concatenar
    subprocess.run(["samba-tool","ou","create","OU="+item[0]])
 """
for item in lst_users:
    #Crear los usuarios (i5) con su contraseña (6)
    subprocess.run(["samba-tool", "user", "create", item[5], item[6]])
    #Activar los usuarios
    subprocess.run(["samba-tool", "user", "enable", item[5]])
    #Añadir a cada usuario a su correspondiente grupo (i8)
    subprocess.run(["samba-tool", "group", "addmembers", item[8],item[5]])
    #Mover cada usuario con el nombre del Dpto correspondiente (i8)
    subprocess.run(['samba-tool', 'user', 'move', item[5],"OU="+item[8]])
    #Hacer que los usuarios del Dpto. informática sean también Admins. de Dominio
    if item[8] == "Informatica":
        subprocess.run(["samba-tool","group","addmembers","Domain Admins", item[5]])
