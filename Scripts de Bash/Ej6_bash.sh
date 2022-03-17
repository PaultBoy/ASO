#!/bin/bash

mkdir $HOME/Bash/diezficheros
cd $HOME/Bash/diezficheros

for ((num=1; num<=10; num++)); do
    touch fichero#$num
done

read -p "¿Quieres borrar los archivos?: [S|N] " borrar

if [[ $borrar == "S" ]]; then
    for ((num=1; num<=10; num++)); do
        rm fichero#$num
    done
fi
