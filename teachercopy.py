#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import getopt
import shutil
from os import listdir
from os import walk
from os.path import isfile
from os.path import join

SRC_BASE = "/Users/flame/Documents/placeholder"

#SRC_DIR = "/Users/flame/alo7-ux/files/output/app/student/v1.6.0/我的_金贝_180607/assets/hdpi/"

DEST_BASE = "/Users/flame/androidaxt/app/src/main/res/"

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
                    print root
                    l.append(join(root, name))

    if(len(l) == 4):
        l.sort()
        index = 0
        for src in l:
            print src
            destPath = join(DEST_BASE + DEST_PATH[index], destName)
            shutil.copyfile(src, destPath)
            index = index + 1


def copyfile(srcName, destName):

    index = 0
    for filename in SRC_PATH:
        srcPath = join(SRC_BASE + filename, srcName)
        print srcPath
        if not isfile(srcPath):
            print "文件不存在，检查路径"
            return
        destPath = join(DEST_BASE + DEST_PATH[index], destName)
        print destName
        print destPath
        shutil.copyfile(srcPath, destPath)
        index = index + 1


def copydir():

    onlyfiles = [f for f in listdir(SRC_DIR) if isfile(join(SRC_DIR, f))]
    for fileName in onlyfiles:
        copyfile(fileName, fileName)


def main(argv):

    try:
        opts, args = getopt.getopt(argv, "hf:s:d:",
                                   ["fname=", "sname=", "dname="])
        srcName = ""
        destName = ""

    except getopt.GetoptError:
        print 'test.py -s <srcname> -d <destname>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -s <srcname> -d <destname>'
            sys.exit()
        elif opt in ("-f","--fname"):
            findfile(arg)
            sys.exit()
        elif opt in ("-s", "--sname"):
            srcName = arg
        elif opt in ("-d", "--dname"):
            destName = arg
            print destName

    findfile(srcName, destName)


if __name__ == "__main__":
    main(sys.argv[1:])
