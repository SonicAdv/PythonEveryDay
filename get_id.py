#!/usr/env/python

import os
import sys

def main():
    if(len(sys.argv) < 2):
        print "%s imput file" % sys.argv[0]
        sys.exit(0)
    input_file = sys.argv[1]

    app_set = set()
    input_fp = open(input_file)
    lines = input_fp.readlines()
    for line in lines:
        lineinfo = line.rstrip('\n')
        app_set.add(lineinfo)

    for newline in app_set:
        print(newline)

if __name__ == "__main__":
    main()
