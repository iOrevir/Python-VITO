#!/usr/bin/env python

import sys

if __name__ == '__main__':
    for line in sys.stdin:
        print(line.rstrip('\n\r').upper())
    print('This is wrong', file = sys.stderr)
