import os
import re

lst = os.listdir("/")

lstDebug = ""

for i in lst:
    if re.search(r'^b',i):
        print(i)