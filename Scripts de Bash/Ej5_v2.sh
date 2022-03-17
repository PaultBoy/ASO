#!/bin/bash

path = "$HOME/Bash/diezficheros"
#Comprobamos si el directorio existe para que no lo cree
if [[ ! -d "$path" ]]; then
    mkdir "$path"
fi

for ((num=1; num<=10; num++)); do
    touch "$/path/fichero#$num"
done
ls -l