import re
import sys
import os


ipadd  = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
obj = open('access.log','r')
for line in obj.readlines():
    mo = ipadd.search(line)
#    if mo:
#        print mo.group()
#    print line

allip = {}
obj = open('access.log','r')
for line in obj.readlines():
    ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
    if ip:
        allip.setdefault(ip[0],0)
        allip[ip[0]] = allip[ip[0]] + 1
       # print ip
print allip

allip = {}
obj = open('access.log','r')
for line in obj.readlines():
    ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
    if ip:
        for i in range(len(ip)):
            allip.setdefault(ip[i],0)
            allip[ip[i]] = allip[ip[i]] + 1
print allip

