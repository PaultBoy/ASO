#!/bin/bash

#Comprobación de argumentos
comprobar_argumentos()
{
    if [[ "$#" != 1 ]]; then
        echo "ERROR: nº de argumentos debe ser 1 (nombre archivo)"
        exit 1
    fi
}
#Llamamos a la función para comprobar argumentos
comprobar_argumentos "$#"
#Comprobación del fichero
if [[ -f "$1" ]]; then
    if [[ -s "$1" ]]; then
        echo "$1 existe y NO está vacío"
    else
        echo "$1 existe pero vacío"
    fi
    if [[ -r "$1" && -w "$1" ]]; then
        echo "Tiene permisos de r y w sobre e fichero $1"
        chmod u+x "$1" && echo "Se ha añadido x sobre $1"
        ls -l $1
    else
        echo "No tienes permisos de r y w sobre $1"
    fi
else
    echo "El fichero no existe"
    touch "$1"
    chmod 600 "$1"
    echo "Comprobamos que se ha creado $1 con permisos r y w: "
    ls -l "$1"
fi