#!/usr/bin/env python
from ttl2md import Converter
from parseArguments import parse_arguments

if __name__ == "__main__":
    args = parse_arguments()
    c = Converter()
    c.readTTL(args.ttlFileName)
#   c.printTTL() # useful for debug
    c.ttl2md()
    if args.mdFileName:
        c.saveMD(args.mdFileName)
    else:
        c.printMD()
