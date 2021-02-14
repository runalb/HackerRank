#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    res= 0

    for x in range(1,10+1):
        res = n * x
        print("{} x {} = {}".format(n,x,res))
