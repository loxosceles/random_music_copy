#!/usr/bin/env python

# Draft for copy random music (CRM)

import os, sys
import random
from distutils.dir_util import copy_tree
import argparse

GB_LIMIT_DEFAULT = 1
total_size = 0
album_count = 0

def gbyte_to_byte(gb):
    return gb * 2**30

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

    parser = argparse.ArgumentParser(description='program description')

    # Add command line arguments, only the path is obligatory
    parser.add_argument('-s', '--sourcedir', help='Source directory or music folder',
            required=True)
    parser.add_argument('-t', '--targetdir', help='Target directory or music folder of device', 
            required=True)
    parser.add_argument('-l', '--limit', help='Limit of data amount to be copied (in GB)')
    
    args = vars(parser.parse_args())

    # Assign source dir
    if args['sourcedir']:
        rootdir = args['sourcedir'].rstrip('/') + '/'
    # Assign targetdir
    if args['targetdir']:
        targetdir = args['targetdir'].rstrip('/') + '/'
    # Define amount of data to be copied. If not given defaulting to 1GB
    if args['limit']:
        upper_limit_gb = int(args['limit'])
    else:
        upper_limit_gb = GB_LIMIT_DEFAULT 

    upper_limit_byte = gbyte_to_byte(upper_limit_gb)

    al = populate_album_list(rootdir)
            
    while total_size < upper_limit_byte:
        album_fullpath = random.choice(al)
        al.remove(album_fullpath)

        print('##############################')
        total_size += get_size(album_fullpath)
        print("Total size (GB): ", total_size / 2**30)
        album_count += 1
        print("Album count: ", album_count)
        print(album_fullpath)
        print(get_size(album_fullpath))
        copy_albums(targetdir, album_fullpath)
