#!/usr/bin/env python
''' Asd asd asd'''

import os

result = []

files = os.listdir('./Vaykky')

for fn in files:
    if not fn.endswith(".txt"):
        continue
    with open('./Vaykky/' + fn, 'rb') as f:
        thing = f.readlines()
        result.extend(thing)



with open("./output-all.txt", 'wb') as o:
    o.writelines(result)
