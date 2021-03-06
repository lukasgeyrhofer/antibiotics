#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--infile")
    parser.add_argument("-o","--outsuffix",default=None,type=str)
    args = parser.parse_args()

    try:    fp = open(args.infile,"r")
    except: raise IOError

    curdata = dict()
    for line in fp.readlines():
        col = line.split()
        if col[0][0] != '#':
            name = col[0].strip('0123456789_')
            if not name in curdata.keys():
                curdata[name] = list()
            curdata[name].append(line)
    fp.close()
    
    if len(curdata) > 0:
        for name in curdata.keys():
            outname = name
            if not args.outsuffix is None:outname += args.outsuffix
            fp = open(outname,'w')
            for line in curdata[name]:
                fp.write(line)
            fp.close()


if __name__ == "__main__":
    main()



