#!/bin/bash

path = "$HOME/Bash/diezficheros"
#Comprobamos si el directorio existe para que no lo cree
#if [[ ! -d "$path" ]]; then
#    mkdir "$path"
#fi
mkdir $HOME/Bash/diezficheros
cd $HOME/Bash/diezficheros

for ((num=1; num<=10; num++)); do
    touch fichero#$num
done
ls -l

read "¿Borrar?" borrar

if [[ borrar = "S" ]]; then
    cd ..
    rm -rf diezficheros
fi 
    