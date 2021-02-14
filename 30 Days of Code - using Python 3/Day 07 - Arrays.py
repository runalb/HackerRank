#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    #print(arr)

    arr.reverse()

    for x in range (0,len(arr)):
        print(arr[x],end=" ")

