#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'mandragora' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY H as parameter.
# 

def mandragora(H):
    # Write your code here
    H.sort()
    n = len(H)
    accumulated_sum = H[n-1]
    temp_sol = 0
    max_sol = n * H[-1]
    previous_sol = max_sol
    k = n-2
    while(k >= 0):
        temp_sol = previous_sol - accumulated_sum
        accumulated_sum = accumulated_sum + H[k]
        temp_sol = temp_sol + (k + 1) * H[k]
        if temp_sol > max_sol:
            max_sol = temp_sol
        previous_sol = temp_sol
        temp_sol = 0
        k = k - 1
    return max_sol

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        H = list(map(int, input().rstrip().split()))

        result = mandragora(H)

        fptr.write(str(result) + '\n')

    fptr.close()
