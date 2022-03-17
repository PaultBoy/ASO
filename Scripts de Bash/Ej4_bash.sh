#!/bin/bash

#read -p "Introduce la ruta de un fichero: " 
#-f comprueba si un archivo existe
if [[ ! -f $1 ]]; then
    echo "El fichero no existe"
    touch $1
    chmod +rw $1
else
#-s comprueba que un archivo contiene datos y no está vacío.
    if [[ -s $1 ]]; then
    echo "El fichero existe y NO está vacío"
        if [[ -r $1 && -w $1 ]]; then
            chmod +x $1
            echo $(ls -l $1| cut -c 1-4)
        fi
    fi
fi
exit 0