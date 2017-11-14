#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 14:01:05 2017

@author: saurabhmehra
"""
import json
import sys
import getopt

Outfile = ''
try:
        optlist, args = getopt.getopt(sys.argv[1:], "w:")
except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)
if (len(optlist) < 1):
        print("Wrong Usage. Use -w <outfile> <infile1>")
        sys.exit(2)
for o, a in optlist:
        if o == "-w":
                Outfile = a
        elif (len(args) < 1):
                print("Wrong Usage. Use -w <outfile> <infile1>")
                sys.exit(2)
        else:
                print("Wrong Usage. Use -w <outfile> <infile1>")
                sys.exit(2)

fileO = open(args[0], 'r')
dump = []

while True:
    temp_string = fileO.readline()
    if temp_string:
        if temp_string.startswith('[') or temp_string.startswith(']'):
            pass
        elif temp_string.startswith('{'):
            dump.append(json.loads(temp_string))
        elif temp_string.startswith(','):
            dump.append(json.loads(temp_string[1:]))
    else:
         break
"""
for i in range(len(dump)):
    print(dump[i]['header']['time'], end=',')
    print(dump[i]['header']['eventId'], end=',')
    print(dump[i]['payload']['enbIp'], end=',')
    print(dump[i]['payload']['enbName'])
"""

file1 = open(Outfile, 'w')
file1.write("Time,eventId,enbIp,enbName")
file1.write('\n')
for i in range(len(dump)):
    file1.write(dump[i]['header']['time'])
    file1.write(',')
    file1.write(dump[i]['header']['eventId'])
    file1.write(',')
    file1.write(dump[i]['payload']['enbIp'])
    file1.write(',')    
    file1.write(dump[i]['payload']['enbName'])
    file1.write('\n')
fileO.close()
file1.close()