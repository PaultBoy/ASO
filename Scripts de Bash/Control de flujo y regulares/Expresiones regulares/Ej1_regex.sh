#!/bin/bash

if [[ $# == 0 ]]; then
	echo "ERROR: No has pasado argumentos"
	exit 1
fi

#set -x
for j in $@; do
    username=$(cat /etc/passwd | grep -o "$j" | uniq)
    if [[ $username == $j ]];then
        echo "$j existe"
    else
        echo "$j no existe"
    fi
done
#set +x
