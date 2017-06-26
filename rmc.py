#!/usr/bin/env python

# draft for copy random music (CRM)
import os, sys
import random

upper_limit_gb = 3
rootdir = '/mnt/DATA/Music/'


def populate_album_list(path):
    full_list = []
    for root, dirs, files in os.walk(rootdir):
        full_list.append(root)
    for i in range(len(full_list) - 1):
        try:
            if full_list[i] in full_list[i + 1]:
                full_list.remove(full_list[i])
        except IndexError:
            return full_list

def get_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

al = populate_album_list(rootdir)
        
for i in range(len(al)):
    artist = random.choice(al)
    al.remove(artist)
    print('_____')
    print(artist)
    print(get_size(artist))

print(al)
