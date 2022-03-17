#!/bin/bash

awk '{ 
    if ($0 ~ /hoge-server systemd-logind[810]: System is powering down./){
        apagados = apagados+1
        print $2 / $1 / $3
    }
    else if ($0 ~ /*.hoge-server sudo: pam_unix(sudo:session): session opened for user root by (uid=0).*/){
        authSU = authSU+1 
    }
    else if ($0 ~ /*.hoge-server sshd[876]: Server listening on 0.0.0.0 port 22\.: session opened for user root by (uid=0).*/){
        authSSH = authSSH+1 
    }
    else if ($0 ~ /*.pam_unix(sshd:session): session opened for user.*/){
        if ($1 ~ /Aug/){
            NumAugSSH=NumAugSSH+1
        }
    }
    else if ($0 ~ /*.COMMAND=/usr/bin/apt install.*/){
        installs=installs+1
    }
    else if ($0 ~ /*.connect_to localhost port (8080|1313): failed.*){
        fails = fails +1
    }

}' auth.log