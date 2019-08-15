#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import sys
from os import listdir
from os import walk
from os.path import isfile
from os.path import join
import argparse
from tinypng import compress_file


SRC_BASE = "/Users/flame/Documents/错题库"

TARGET_PATH = ["/hdpi", "/xhdpi", "/xxhdpi", "/xxxhdpi"]


def compress_drawable(fileName):
    l = []
    for root, dirs, files in walk(SRC_BASE):
        for name in files:
            if(name == fileName):
                if(root[root.rindex('/'):] in TARGET_PATH):
                    print(root)
                    l.append(join(root, name))

    if(len(l) == 4):
        for src in l:
            compress_file(src, -1)
           


def main():
    

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="the filename to compress")
    args = parser.parse_args()
    compress_drawable(args.filename)


if __name__ == "__main__":
    main()
