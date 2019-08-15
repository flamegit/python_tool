#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import shutil
from os import listdir
from os import walk
from os.path import isfile
from os.path import join
import argparse
from config import readConifg

DRAWABLE_PATH = ["hdpi", "xhdpi", "xxhdpi", "xxxhdpi"]

def findfile(fileName, destName,compress = False):
    l = []
    for root, dirs, files in walk(SRC_BASE): 
        for name in files:
            if(name == fileName):
                if(root[root.rindex('/') + 1:] in DRAWABLE_PATH):
                    print (root)
                    if(compress):
                        print("compress image")
                    l.append(join(root, name))

    if(len(l) == 4):
        l.sort()
        index = 0
        for src in l:
            destPath = join('{}{}{}'.format(DEST_BASE,'/drawable-',DRAWABLE_PATH[index]), destName)
            shutil.copyfile(src, destPath)
            index = index + 1

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("src", help="the source file")
    parser.add_argument("dest", help="the destination file")
    parser.add_argument("-c", "--compress", help="compress or not",action="store_true")
    parser.add_argument("-s", "--section", help="指定配置文件section",default ='student')

    args = parser.parse_args()
    config_info = readConifg(args.section)
    global SRC_BASE, DEST_BASE
    SRC_BASE = config_info.src_path
    DEST_BASE = config_info.dest_path
    findfile(args.src, args.dest,args.compress)


if __name__ == "__main__":
    main()
