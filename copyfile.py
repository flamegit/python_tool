#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import sys
import getopt
import shutil
from os import listdir
from os import walk
from os.path import isfile
from os.path import join

import argparse

#SRC_BASE = "/Users/flame/outputs/files/student/v1.10.0/首页_20181030/"

SRC_BASE = "/Users/flame/Documents/v1.15.0"

SRC_DIR = "/Users/flame/alo7-ux/files/output/app/student/v1.6.0/我的_金贝_180607/assets/hdpi/"

DEST_BASE = "/Users/flame/alo7-student/app/src/main/res/"

DEST_PATH = ["drawable-hdpi/", "drawable-xhdpi/", "drawable-xxhdpi/",
                               "drawable-xxxhdpi/"]

SRC_PATH = ["hdpi/", "xhdpi/", "xxhdpi/", "xxxhdpi/"]

TARGET_PATH = ["/hdpi", "/xhdpi", "/xxhdpi", "/xxxhdpi"]


def findfile(fileName, destName):
    l = []
    for root, dirs, files in walk(SRC_BASE):
        for name in files:
            if(name == fileName):
                if(root[root.rindex('/'):] in TARGET_PATH):
                    print (root)
                    l.append(join(root, name))

    if(len(l) == 4):
        l.sort()
        index = 0
        for src in l:
            print(src)
            destPath = join(DEST_BASE + DEST_PATH[index], destName)
            shutil.copyfile(src, destPath)
            index = index + 1


def copyfile(srcName, destName):

    index = 0
    for filename in SRC_PATH:
        srcPath = join(SRC_BASE + filename, srcName)
        print (srcPath)
        if not isfile(srcPath):
            print ("文件不存在，检查路径")
            return
        destPath = join(DEST_BASE + DEST_PATH[index], destName)
       
        shutil.copyfile(srcPath, destPath)
        index = index + 1


def copydir():

    onlyfiles = [f for f in listdir(SRC_DIR) if isfile(join(SRC_DIR, f))]
    for fileName in onlyfiles:
        copyfile(fileName, fileName)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("src", help="the source file")
    parser.add_argument("dest", help="the destination file")
    args = parser.parse_args()

    findfile(args.src, args.dest)


if __name__ == "__main__":
    main()
