#!/usr/bin/env python
# Draft for copy random music (CRM)
import os, sys
import random
from distutils.dir_util import copy_tree

upper_limit_gb = 1
upper_limit_byte = upper_limit_gb * 10**9
total_size = 0
album_count = 0
rootdir = '/mnt/DATA/Music/'
targetdir = '/mnt/DATA/test/'
album_list = []


USAGE = """
        USAGE:
        crm SOURCE TARGET

        SOURCE: source directory
        TARGET: target directory
        """
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

def extract_band_name(path):
    return path.split(rootdir)[1].split('/')[0]

def extract_album_name(path):
    return path.split('/')[-1]

def copy_albums(targetdir, album):
    targetdir_band = targetdir + extract_band_name(album) + '/' + extract_album_name(album)

    print("Album: ", album)
    print("targetdir_band: ", targetdir_band)
    print('##############################')
    copy_tree(album, targetdir_band)

if __name__ == "__main__":

    if len(sys.argv) is not 3:
        print(USAGE)
        sys.exit(1)
    else:
        rootdir = sys.argv[1]
        targetdir = sys.argv[2]

al = populate_album_list(rootdir)
        
while total_size < upper_limit_byte:
    album_fullpath = random.choice(al)
    al.remove(album_fullpath)
    #album_list.append(album_fullpath)
    #print(extract_band_name(album_fullpath))
    #print("album_fullpath list: ", album_list)
    #print(targetdir_band)

    print('##############################')
    total_size += get_size(album_fullpath)
    print("Total size (GB): ", total_size / 10**9)
    album_count += 1
    print("Album count: ", album_count)
    print(album_fullpath)
    print(get_size(album_fullpath))
    copy_albums(targetdir, album_fullpath)

#print(al)
#print()
#print(album_list)
