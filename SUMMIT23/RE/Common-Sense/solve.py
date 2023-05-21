#!/usr/bin/env python3

# flag: SummitCTF{p35Ky_fuNc710N_C4115}

from math import floor
import base64

flag_txt_1 = open('flag.txt', 'r').read()

flag_txt = ''
for x in range(1,len(flag_txt_1),2):
    flag_txt += flag_txt_1[x]
    flag_txt += flag_txt_1[x-1]

key = 'jh8x5j$0'
pairs = (2,4)

length = floor(len(flag_txt) / 2)
flag = ''
for x in range(0, length):
    flag += chr(ord(flag_txt[x]) ^ len(key))
for x in range(length, len(flag_txt)):
    flag += chr(ord(flag_txt[x]) ^ ord(key[pairs[0]]) + ord(key[pairs[1]]) - 0x69)

print(base64.b64decode(flag).decode())
