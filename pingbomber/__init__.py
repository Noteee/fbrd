import re
import os

fr = open("file.txt", "w")
fr.write("")
fr.close()

os.system("nmap -sP 192.168.1.0/24 >> file.txt")

fr = open("file.txt", "r")
a = fr.read()

regfind = re.findall("\w+\.\w+\.\w+\.\w+", a)


def clearcurrentips():
    global fr
    fr = open("currentips.txt", "w")
    fr.write("")
    fr.close()


clearcurrentips()

for i in regfind:
    os.system("avahi-resolve-address " + str(i) + " >> currentips.txt")
