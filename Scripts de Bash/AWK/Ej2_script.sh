#!/bin/bash
case $1 in

    "1")find / -size +10M -print0;;
    "2")find /var/log -name "*.log" | xargs -0 tar -zcvf $HOME/log.tar.gz;;
    "3")find /home/pablo -maxdepth 1 -name "*.sh"  | xargs -0 wc -l;;
esac