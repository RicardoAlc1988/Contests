#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def abbreviation(a, b):
    # Write your code here
    n = len(a) + 1
    m = len(b) + 1
    # size of matrix n x m
    sol = [ [ 0 for i in range(n) ] for j in range(m) ]
    # base cases: filling of 1st row
    sol[0][0] = 1
    for i in range(1, n):
     if a[i-1].islower():
        sol[0][i] = sol[0][i-1]
    else:
         sol[0][i] = 0
    
    # General case
    for i in range(1,m):
      for j in range(1,n):
        temp = sol[i-1][j-1] * (a[j-1].upper() == b[i-1])
        if a[j-1].islower():
          temp = max(temp,sol[i][j-1])
        sol[i][j] = temp
    if sol[m-1][n-1] == 1:
        out = 'YES'
    else:
        out = 'NO'
    return out
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
