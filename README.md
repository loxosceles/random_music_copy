# Copy Random Music

## Description

This script copies files from your music folder into a music folder on a mobile
device randomly.

It preserves file organization on the target folder assuming that the following
hierarchy is in place on the source folder:

    Top-Level folder
      Artist name
        Album name
          Music files

  ![Folder Hierarchy](https://raw.githubusercontent.com/loxosceles/random_music_copy/master/doc/Selection_038.jpg)

It will then pick randomly from all albums on the source and copy it to the target
creating a folder for the artist (only if it doesn't exist already).

A transfer data limit (in GB) can be set, otherwise it will default to 1 GB. When the
limit is reached on the target, no more folders will be copied.


## Usage

    crm [-h] -s SOURCEDIR -t TARGETDIR [-l LIMIT]

## Example

Copy from */home/user/Music* to */media/phone-xyz/Music* until 1 GB limit is reached

    crm -s /home/user/Music -t /media/phone-xyz/Music

Copy 3 GB from */home/user/Music* to */media/phone-xyz/Music*

    crm -s /home/user/Music -t /media/phone-xyz/Music -l 3

## To-Do

* Copying only music files (no images)

