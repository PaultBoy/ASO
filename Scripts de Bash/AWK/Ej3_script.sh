#!/bin/bash
ip address show | grep -E -o '(([0-9a-f][0-9a-f]):){5}(([0-9a-f][0-9a-f]))' | awk '{if($0 !~ /ff:ff:ff:ff:ff:ff|00:00:00:00:00:00/){ print $0 }}'