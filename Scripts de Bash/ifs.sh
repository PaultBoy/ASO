#!/bin/bash

if [[ $# != 1 ]]; then
	echo "Error de argumentos"
	exit 1
fi
set -x
#file="$HOME/helloworld.sh"
file="$1"

if [[ -f "$file" ]]; then

	echo "Fichero existe"
	ls -ls "$file"
set +x
else
	echo "Fichero no existe"
	touch "$file"
	ls -l "$file"
fi

